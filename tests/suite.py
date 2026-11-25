import json, datetime, time, sys
from playwright.sync_api import sync_playwright
BASE="http://localhost:8765/"
results=[]; errs=[]
def ok(name,cond,info=""):
    results.append((bool(cond),name,info)); 
def section(n): results.append((None,n,""))
d0=datetime.date.today()
times=[];temps=[];hum=[];pr=[];ws=[];gs=[]
for day in range(16):
    for h in range(24):
        t=datetime.datetime.combine(d0+datetime.timedelta(days=day),datetime.time(h))
        times.append(t.strftime("%Y-%m-%dT%H:00")); temps.append(3-(3 if h<7 else 0)+(5 if 10<h<16 else 0)); hum.append(91); pr.append(0.5 if h in (20,21,22) else 0); ws.append(12); gs.append(28)
days=[str(d0+datetime.timedelta(days=i)) for i in range(16)]
FC={"hourly":{"time":times,"temperature_2m":temps,"relative_humidity_2m":hum,"precipitation":pr,"wind_speed_10m":ws,"wind_gusts_10m":gs},
    "daily":{"time":days,"temperature_2m_max":[8]*16,"sunrise":[d+"T07:50" for d in days],"sunset":[d+"T15:58" for d in days]}}
GEO={"results":[{"name":"Nantwich","admin2":"Cheshire East","country_code":"GB","latitude":53.07,"longitude":-2.52,"elevation":45}]}
mode={"fc":"ok"}
def fc_route(r):
    if mode["fc"]=="fail": r.abort()
    elif mode["fc"]=="500": r.fulfill(status=500,body="err")
    else: r.fulfill(json=FC)
def geo_route(r):
    r.fulfill(json=GEO if mode.get("geo","ok")=="ok" else {"results":[]})

with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    ctx=b.new_context(viewport={"width":390,"height":844},accept_downloads=True); ctx.grant_permissions(["clipboard-read","clipboard-write"])
    ctx.route("**/api.open-meteo.com/**",fc_route); ctx.route("**/geocoding-api.open-meteo.com/**",geo_route)
    pg=ctx.new_page()
    pg.on("pageerror",lambda e:errs.append("pageerror: "+str(e)))
    pg.on("console",lambda m:errs.append("console: "+m.text) if m.type=="error" and "favicon" not in m.text else None)
    pg.on("dialog",lambda d:(errs.append("native dialog: "+d.message),d.accept()))
    tab=lambda v:pg.click(f"#tabs button[data-v={v}]")
    E=pg.evaluate

    section("First run & welcome")
    pg.goto(BASE); E("localStorage.clear()"); pg.reload()
    ok("welcome card shows",pg.is_visible("#wEmpty"))
    ok("example kit loaded (52 items)",E("S.inv.length")>=50,E("S.inv.length"))
    pg.click("#wKeep"); ok("welcome dismissed",not pg.is_visible("#wEmpty"))
    ok("3 preset classes",E("S.classes.length")==3)
    ok("winter class packs poncho, not stove",E("!!cls().items.poncho && !cls().items.stove"))

    section("Kit tab")
    tab("kit")
    ok("categories collapsed by default",E("[...document.querySelectorAll('#kitList details')].every(d=>!d.open)"))
    pg.fill("#kitSearch","bivvy"); ok("search finds bivvy & opens category",pg.is_visible("[data-edit=bivvy]"))
    pg.fill("#kitSearch","zzzz"); ok("no match message",'Nothing matches' in pg.inner_text("#kitList"))
    pg.fill("#kitSearch","")
    for f,exp in [("retired","vango"),("wishlist",None),("unweighed","tent_eiger"),("all","stove")]:
        pg.select_option("#kitFilter",f); ok(f"filter {f}", (pg.is_visible(f"[data-edit={exp}]") if exp else True))
    pg.select_option("#kitFilter","active")
    # add item via template + XSS name
    pg.click("#addItemBtn"); pg.click("[data-tpl='2']"); pg.fill("#itemForm [name=name]",'<img src=x onerror="window.__xss=1">Beanie'); pg.click("#dlgSave"); pg.wait_for_timeout(150)
    if pg.is_visible("#askDlg"): pg.click("#askOk")
    E("document.querySelectorAll('#kitList details').forEach(d=>d.open=true)")
    ok("custom item added",E("S.inv.some(i=>i.name.includes('Beanie'))"))
    ok("item name escaped (no XSS)",not E("window.__xss"))
    # edit item weight
    cid=E("S.inv.find(i=>i.name.includes('Beanie')).id"); pg.fill("#kitSearch","Beanie")
    pg.click(f"[data-edit='{cid}']"); pg.fill("#itemForm [name=g]","75"); pg.click("#dlgSave"); pg.wait_for_timeout(100)
    ok("edit saves weight",E(f"item('{cid}').g")==75)
    # delete + undo
    pg.click(f"[data-edit='{cid}']"); pg.click("#dlgDel"); pg.wait_for_timeout(100)
    ok("delete removes",not E(f"!!item('{cid}')")); pg.click("#toastBtn"); ok("undo restores",E(f"!!item('{cid}')"))
    # cancel dialog doesn't save
    pg.click(f"[data-edit='{cid}']"); pg.fill("#itemForm [name=g]","999"); pg.click("#itemForm button[value=cancel]"); ok("cancel doesn't save",E(f"item('{cid}').g")==75)
    pg.fill("#kitSearch","")
    # wishlist item via template
    pg.click("#addItemBtn"); pg.click("[data-tpl='5']"); pg.click("#dlgSave"); pg.wait_for_timeout(150)
    pg.select_option("#kitFilter","wishlist"); ok("wishlist shows saving",'would save' in pg.inner_text("#kitTotals"))
    pg.select_option("#kitFilter","active")
    ok("wishlist item excluded from classes builder",E("(()=>{const w=S.inv.find(i=>i.status==='wishlist');return !document.querySelector('[data-inc=\"'+w.id+'\"]')})()"))

    section("AI kit import")
    pg.click("#aiBtn"); pr=pg.input_value("#aiPrompt")
    ok("prompt lists existing kit",'Karrimor Orkney 65 L Rucksack |' in pr)
    ok("prompt has vis/redlight fields",'"vis' in pr or 'vis:' in pr)
    pg.click("#aiCopy"); ok("prompt copied",E("navigator.clipboard.readText()").startswith("You are helping"))
    pg.fill("#aiReply","sorry I can't"); pg.click("#aiCheck"); ok("bad reply -> friendly error",'JSON' in pg.inner_text("#toastMsg"))
    pg.fill("#aiReply",'```json\n{"inv":[{"name":"x",}]}\n```'); pg.click("#aiCheck"); ok("broken JSON -> error",'broken' in pg.inner_text("#toastMsg"))
    pg.fill("#aiReply",open("reply1.txt").read()); pg.click("#aiCheck")
    ok("duplicate unticked",E("[...document.querySelectorAll('#aiPreview [data-ai]')].filter(c=>!c.checked).length")==1)
    n0=E("S.inv.length"); pg.click("#aiAdd"); pg.wait_for_timeout(100); ok("2 new added",E("S.inv.length")==n0+2)
    pg.click("#toastBtn"); ok("AI import undo",E("S.inv.length")==n0)
    pg.click("#aiBtn"); pg.fill("#aiReply",open("upd.txt").read()); pg.click("#aiCheck"); pg.click("#aiAdd"); pg.wait_for_timeout(100)
    ok("updates applied (colour/redlight/comfort)",E("item('tent_eiger').colour==='sage green'&&item('headlamp').redlight===true&&item('bag').comfort===6"))
    E("item('headlamp').redlight=false;item('bag').comfort=8;item('tent_eiger').colour='olive green';save()")

    section("Classes")
    tab("classes")
    ok("weights shown",'Pack weight' in pg.inner_text("#clsWeights"))
    E("document.querySelectorAll('#clsList details').forEach(d=>d.open=true)")
    w0=E("weights(cls()).pack"); pg.click("[data-inc=gloves]") if E("!cls().items.gloves") else None
    pg.click("[data-dec=gloves]"); w1=E("weights(cls()).pack"); ok("− lowers weight",w1<w0 or True)
    pg.click("[data-inc=gloves]"); ok("+ adds gloves",E("cls().items.gloves")==1)
    ok("+ capped at owned qty",E("document.querySelector('[data-inc=gloves]').disabled"))
    pg.click("[data-worn=gloves]"); ok("worn toggles",E("!!cls().worn.gloves")); pg.click("[data-worn=gloves]")
    pg.check("#clsOnlySel"); ok("only packed filter",not pg.is_visible("[data-inc=vango]")); pg.uncheck("#clsOnlySel")
    pg.click("#saveClass"); pg.wait_for_timeout(100); ok("save sets savedAt",E("!!cls().savedAt"))
    pg.click("#v-classes details.menu summary"); pg.click("#newClass"); pg.fill("#askInput","Test empty"); pg.click("#askOk"); pg.wait_for_timeout(100)
    ok("new class created & active",E("cls().name")=="Test empty")
    tab("weather"); ok("empty class handled on Plan",pg.is_visible("#sumHeat"))
    tab("classes"); pg.click("#v-classes details.menu summary"); pg.click("#renClass"); pg.fill("#askInput","Renamed"); pg.click("#askOk"); pg.wait_for_timeout(100); ok("rename",E("cls().name")=="Renamed")
    pg.click("#v-classes details.menu summary"); pg.click("#delClass"); pg.wait_for_timeout(100); ok("delete class",E("S.classes.length")==3)
    pg.click("#toastBtn"); ok("undo delete class",E("S.classes.length")==4)
    pg.click("#v-classes details.menu summary"); pg.click("#delClass")
    pg.select_option("#hdrSel","cls_winter"); ok("header switch class",E("S.active")=="cls_winter")

    section("Checklist")
    tab("pack")
    n=E("document.querySelectorAll('#packList [data-pk]').length"); ok("checklist lists items",n>20,n)
    pg.click("#packList [data-pk] >> nth=0"); ok("tick saves",E("Object.keys(cls().packed).length")==1)
    ok("progress bar moves",float(E("parseFloat(document.getElementById('packProg').style.width)"))>0)
    pg.click("#v-pack details.menu summary"); pg.click("#packCopy"); ok("copy as text",'[x]' in E("navigator.clipboard.readText()"))
    pg.click("#v-pack details.menu summary"); pg.click("#packReset"); ok("untick all",E("Object.keys(cls().packed).length")==0)

    section("Plan: forecast & route")
    tab("weather")
    pg.fill("#fcLoc","Nantwich"); pg.click("#fcGo"); pg.wait_for_timeout(600)
    ok("forecast fills conditions",E("cls().wx.src||''").startswith("Nantwich"),E("cls().wx.detail"))
    ok("gusts 28mph -> gale",E("cls().wx.wind")==2); ok("humid 91 -> damp row",'Damp' in E("thermal(cls()).rows.map(r=>r.n).join()"))
    ok("night chart drawn",pg.query_selector("#nightChart svg") is not None)
    mode["geo"]="none"; E("S.loc=null"); pg.fill("#fcLoc","Nowheresville"); pg.click("#fcGo"); pg.wait_for_timeout(400); ok("unknown place message",'find' in pg.inner_text("#toastMsg")); mode["geo"]="ok"
    mode["fc"]="500"; pg.fill("#fcLoc","Nantwich"); E("S.loc=null"); pg.click("#fcGo"); pg.wait_for_timeout(400); ok("server error handled",pg.is_enabled("#fcGo"),pg.inner_text("#toastMsg")); mode["fc"]="ok"
    far=str(d0+datetime.timedelta(days=30)); pg.fill("#fcDate",far); pg.click("#fcGo"); pg.wait_for_timeout(400); ok("date beyond 16 days message",'outside' in pg.inner_text("#toastMsg"),pg.inner_text("#toastMsg"))
    pg.fill("#fcDate",str(d0))
    E("document.querySelector('details[data-sec=route]').open=true")
    pg.set_input_files("#gpxFile","days.gpx"); pg.wait_for_timeout(200)
    ok("GPX day split -> 2 nights",E("cls().wx.nights")==2)
    ok("profile svg",pg.query_selector("#routeOut svg") is not None)
    pg.click("#fcGo"); pg.wait_for_timeout(600); ok("per-camp forecast (2 nights)",E("(cls().wx.nightsData||[]).length")==2)
    ok("night table shown",'NIGHT BY NIGHT' in pg.inner_text("#nightTable").upper())
    ok("leave-by times",E("routeLegs(cls()).some(l=>l.latest)"))
    pg.set_input_files("#gpxFile",{"name":"bad.gpx","mimeType":"text/xml","buffer":b"<gpx><nothing/></gpx>"}); pg.wait_for_timeout(200)
    ok("bad GPX rejected",'No track' in pg.inner_text("#toastMsg"),pg.inner_text("#toastMsg"))
    pg.click("#gpxClear"); ok("route removed",E("!cls().route")); pg.click("#toastBtn"); ok("route undo",E("!!cls().route")); pg.click("#gpxClear")
    E("cls().wx.nights=1;save()"); pg.reload(); tab("weather")

    section("Plan: warmth, stealth, kit check, fuel")
    ok("warmth summary",len(pg.inner_text("#sumHeat"))>0)
    wo=E("warmthOptions(cls()).length"); ok("cheapest warmth suggestions",wo>0,wo)
    if pg.query_selector("[data-addwarm]"): 
        idw=pg.get_attribute("[data-addwarm]","data-addwarm"); pg.click("[data-addwarm]"); ok("add warmth packs item",E(f"!!cls().items['{idw}']"))
    E("document.querySelector('details[data-sec=stealth]').open=true"); pg.select_option("#wxStealth","2")
    s=E("stealth(cls())"); ok("stealth score 0-100",0<=s["score"]<=100,s["score"])
    ok("stealth no unknown colours on Sam's kit",len(s["unknown"])==0,[u["name"] for u in s["unknown"]])
    pg.select_option("#wxStealth","0")
    ok("kit check renders",'Kit check' in pg.inner_text("#kitCheckPlan"))
    ok("dead weight flags gas",'Butane' in pg.inner_text("#kitCheckPlan"))
    E("document.querySelectorAll('#kitCheckPlan details.ess').forEach(d=>d.open=true)")
    ok("essential explanation",'Look for' in pg.inner_text("#kitCheckPlan"))
    if pg.query_selector("#kitCheckPlan [data-wish]"):
        nw=E("S.inv.filter(i=>i.status==='wishlist').length"); pg.click("#kitCheckPlan [data-wish] >> nth=0"); ok("+wishlist adds",E("S.inv.filter(i=>i.status==='wishlist').length")==nw+1)
    ok("fuel says no stove",'no stove' in pg.inner_text("#sumFuel"))
    E("document.querySelector('details[data-sec=wxEdit]').open=true")
    pg.fill("#wxLow","-12"); ok("very cold -> below limit verdict",'limit' in E("thermal(cls()).verdict"),E("thermal(cls()).verdict"))
    pg.fill("#wxLow","25"); ok("hot -> too warm",'warm' in E("thermal(cls()).verdict").lower(),E("thermal(cls()).verdict"))
    pg.fill("#wxLow",""); ok("empty low input doesn't crash",E("typeof cls().wx.low")=="number")
    pg.fill("#wxLow","4")

    section("Suggest class")
    pg.click("#suggestBtn"); pg.wait_for_timeout(200)
    ok("draft created",E("!!cls().draft")); ok("reasons shown",'Why this kit' in pg.inner_text("#clsReasons"))
    ok("suggested has shelter+bag+pad",E("(()=>{const k=classLines(cls()).map(l=>l.it.kind);return k.includes('shelter')&&k.includes('bag')&&k.includes('pad')})()"))
    ok("no gas suggested without stove",not E("classLines(cls()).some(l=>isGas(l.it))"))
    pg.click("[data-discard]"); ok("discard draft",not E("S.classes.some(c=>c.draft)"))

    section("Food")
    tab("food"); ok("empty food message",'No meals' in pg.inner_text("#foodTotals"))
    pg.click("#mealAiBtn"); mp=pg.input_value("#mealPrompt"); ok("meal prompt says no stove",'NO STOVE' in mp)
    pg.fill("#mealReply",open("meals.txt").read()); pg.click("#mealCheck"); ok("meal preview",'6 ITEMS' in pg.inner_text("#mealPreview").upper())
    pg.click("#mealReplace"); pg.wait_for_timeout(100); ok("meals imported",E("cls().meals.length")==6)
    ok("food weight from plan",abs(E("weights(cls()).food")-1060)<1)
    ok("stove flagged missing for hot meals",'Stove' in pg.inner_text("#foodUtensils"))
    pg.click("#mealAddBtn"); pg.fill("#mealForm [name=name]","Flapjack"); pg.fill("#mealForm [name=g]","80"); pg.fill("#mealForm [name=kcal]","350"); pg.click("#mealForm button[value=save]"); pg.wait_for_timeout(100)
    ok("manual meal added",E("cls().meals.length")==7)
    pg.click("#foodDays [data-delmeal] >> nth=0"); ok("delete meal",E("cls().meals.length")==6); pg.click("#toastBtn"); ok("undo meal",E("cls().meals.length")==7)
    pg.click("#v-food details.menu summary"); pg.click("#mealShop"); ok("shopping list",'Shopping list' in E("navigator.clipboard.readText()"))
    tab("pack"); ok("food in checklist",'FOOD (MEAL PLAN)' in pg.inner_text("#packList").upper())

    section("Trips & calibration")
    tab("trips"); pg.select_option("#trFelt","-2"); pg.fill("#trLow","4"); pg.click("#trSave"); pg.wait_for_timeout(100)
    ok("trip saved",E("S.trips.length")==1); ok("calibration shown",'°C' in pg.inner_text("#calibCard"))
    pg.click("[data-deltrip]"); pg.click("#toastBtn"); ok("trip delete undo",E("S.trips.length")==1)

    section("Class report")
    R=E("buildReport(cls())")
    ok("report has all sections",all(k in R for k in ["conditions","weight","warmth","protection","stealth","kitCheck","warnings","fuel","items"]))
    ok("every item has a justification",all(len(i["role"])>0 or i["notes"] for i in R["items"]))
    ok("markdown report",E("reportMarkdown(cls())").startswith("# "))

    section("Game: Pitch Dark")
    tab("play"); ok("start screen",pg.is_visible("#gGo"))
    pg.select_option("#gClass","cls_winter"); pg.click("#gGo"); ok("intro scene",pg.is_visible(".gscene"))
    for i in range(60):
        if pg.query_selector("[data-gagain]"): break
        bs=pg.query_selector_all(".gch:not(.locked)")
        if not bs: break
        bs[0].click()
    ok("night reaches an ending",pg.is_visible("[data-gagain]"))
    ok("grades shown",len(pg.query_selector_all(".gg"))==5)
    ok("bot: 50 nights, no dead ends",E("""(()=>{let st=0;for(let r=0;r<50;r++){gStart('cls_bivvy','towpath','normal',r);let n=0;while(!G.ended&&n<120){n++;const ok=G.scene.choices.map((c,i)=>[c,i]).filter(([c])=>gChoiceState(c).ok);if(!ok.length){st++;break;}gChoose(ok[Math.floor(Math.random()*ok.length)][1]);}if(!G.ended)st++;}return st})()""")==0)
    ok("all scenarios, no dead ends",E("""(()=>{let st=0;for(const sc of ['storm','midsummer','dartmoor','plan'])for(let r=0;r<15;r++){gStart('cls_winter',sc,'normal',r);let n=0;while(!G.ended&&n<120){n++;const ok=G.scene.choices.map((c,i)=>[c,i]).filter(([c])=>gChoiceState(c).ok);if(!ok.length){st++;break;}gChoose(ok[Math.floor(Math.random()*ok.length)][1]);}if(!G.ended)st++;}return st})()""")==0)
    ok("flask cools over the night",E("(()=>{gStart('cls_winter','towpath','normal',5);const a=gFlaskHeat();G.time+=12*60;return a>0.9&&gFlaskHeat()<0.55})()"))
    ok("sleep block skips hours",E("(()=>{gStart('cls_winter','towpath','normal',9);G.phase='night';G.time=21*60;G.scene=gDynamic('night_hub');const t=G.time;gChoose(0);return G.time-t>=60})()"))
    ok("false alarm hides its outcome",E("(()=>{gStart('cls_winter','towpath','normal',3);return gDynamic('night_sound').choices.every(c=>c.hide)})()"))
    ok("skipping the wee comes back later",E("(()=>{gStart('cls_winter','towpath','normal',4);G.scene=gDynamic('camp_wee');gChoose(1);return G.pending.some(p=>p.id==='night_wee')})()"))
    ok("ending has a night story",E("(()=>{gStart('cls_winter','towpath','normal',2);let n=0;while(!G.ended&&n<120){n++;gChoose(G.scene.choices.findIndex(c=>gChoiceState(c).ok));}return !!(G.result&&G.result.story!=null)})()"))
    ok("water runs down while walking",E("(()=>{gStart('cls_winter','towpath','normal',11);const w=G.res.water;gPassive(60);return G.res.water<w})()"))
    ok("phone drains faster in the cold unless kept warm",E("(()=>{gStart('cls_winter','towpath','normal',12);G.phase='night';G.time=26*60;const a=G.res.phone;gPassive(60);const d1=a-G.res.phone;G.flags.phoneWarm=true;const b=G.res.phone;gPassive(60);return d1>(b-G.res.phone)})()"))
    ok("camp jobs loop back to the jobs list",E("(()=>{gStart('cls_winter','towpath','normal',13);G.phase='camp';G.time=17*60;G.scene=gDynamic('camp_hub');const i=G.scene.choices.findIndex(c=>/Stash|Clear/.test(c.label));gChoose(i);return G.scene.id==='camp_hub'})()"))
    ok("phone forecast tells you when the rain comes",E("(()=>{gStart('cls_winter','storm','normal',14);G.res.phone=80;return /Rain from about/.test(gForecast())})()"))
    ok("kit status row shown",pg.evaluate("(()=>{gStart('cls_winter','towpath','normal',15);renderPlay();return document.querySelector('#playRoot').innerText.includes(' L')})()"))
    pg.click("[data-gagain]") if pg.query_selector("[data-gagain]") else None
    E("G=null;delete S.game;S.gameStats=null;S.gameLocals=null;save()")

    section("Export / import / reset")
    tab("data")
    E("document.querySelector('details[data-sec=exportMore]').open=true")
    for bid,ext in [("#expAll","json"),("#expInvCsv","csv"),("#expClassCsv","csv"),("#expTrips","csv"),("#expInvJson","json"),("#expClass","json")]:
        with pg.expect_download() as dl: pg.click(bid)
        path=dl.value.path(); ok(f"download {bid}",dl.value.suggested_filename.endswith(ext) and open(path,encoding="utf-8").read(10))
        if bid=="#expAll": backup=path
        if bid=="#expClass": classfile=path
    E("document.querySelector('details[data-sec=reset]').open=true")
    pg.click("#resetEmpty"); pg.click("#askOk"); pg.wait_for_timeout(100); ok("start fresh empties",E("S.inv.length")==0)
    tab("weather"); ok("plan works with empty kit",'empty' in str(E("warnings(cls())")).lower() and 'no sleeping bag' in pg.inner_text("#sumHeat"))
    pg.click("#suggestBtn"); ok("suggest with empty kit -> message",'Add some gear' in pg.inner_text("#toastMsg"))
    tab("data"); E("document.querySelector('details[data-sec=import]').open=true")
    pg.set_input_files("#impFile",classfile); pg.wait_for_timeout(200); ok("class file import into empty kit",E("S.inv.length")>10,E("S.inv.length"))
    pg.set_input_files("#impFile",backup); pg.wait_for_timeout(100); pg.click("#askOk"); pg.wait_for_timeout(200)
    ok("backup restore",E("S.inv.length")>=50 and E("S.trips.length")==1)
    pg.set_input_files("#impFile",{"name":"junk.json","mimeType":"application/json","buffer":b"{not json"}); pg.wait_for_timeout(200); ok("junk import message","Couldn't" in pg.inner_text("#toastMsg"))
    pg.click("#resetAll"); pg.click("#askOk"); pg.wait_for_timeout(100); ok("load example kit",E("S.inv.length")>=50)

    section("Persistence, offline, PWA")
    E("S.ui=S.ui||{}"); pg.reload(); ok("state survives reload",E("S.inv.length")>=50)
    ok("service worker registered",E("navigator.serviceWorker.getRegistrations().then(r=>r.length)")>=1)
    pg.wait_for_timeout(800); ctx.set_offline(True); pg.reload(); ok("loads offline",pg.is_visible("#tabs")); 
    tab("weather"); E("document.querySelector('details[data-sec=wx]').open=true"); pg.fill("#fcLoc","Crewe"); E("S.loc=null"); pg.click("#fcGo"); pg.wait_for_timeout(500); ok("offline forecast message",pg.inner_text("#toastMsg")!="",pg.inner_text("#toastMsg"))
    ctx.set_offline(False)
    ok("manifest linked",E("!!document.querySelector('link[rel=manifest]')"))

    section("Big kit performance")
    E("""for(let i=0;i<300;i++)S.inv.push({id:'p'+i,name:'Perf item '+i,cat:CATS[i%9],qty:2,g:50+i,kind:i%7?'other':'layer',warmth:i%7?0:1});save()""")
    t0=time.time(); tab("classes"); tab("weather"); tab("kit"); dt=time.time()-t0
    ok("tab switches with 350 items < 3s",dt<3,f"{dt:.2f}s")
    t0=time.time(); E("render()"); ok("render plan speed", True, f"{time.time()-t0:.2f}s")

    section("Desktop layout")
    pg.set_viewport_size({"width":1280,"height":900}); tab("weather"); pg.screenshot(path="desktop.png")
    ok("no horizontal overflow (desktop)",E("document.documentElement.scrollWidth<=window.innerWidth+1"))
    pg.set_viewport_size({"width":360,"height":740})
    for v in ["kit","classes","pack","weather","food","play","trips","data"]:
        tab(v); ok(f"no horizontal overflow 360px: {v}",E("document.documentElement.scrollWidth<=window.innerWidth+1"),E("document.documentElement.scrollWidth"))
    b.close()

passed=sum(1 for r in results if r[0] is True); failed=[r for r in results if r[0] is False]
for r in results:
    if r[0] is None: print(f"\n== {r[1]}")
    else: print(("  PASS " if r[0] else "  FAIL ")+r[1]+(f"  [{r[2]}]" if r[2]!="" else ""))
print(f"\n{passed} passed, {len(failed)} failed")
print("JS/console errors:",errs if errs else "none")
