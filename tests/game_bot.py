import json
from playwright.sync_api import sync_playwright
errs=[]
BOT="""(args)=>{
 const [classId,scen,diff,strategy,runs]=args; const res={}; const turns=[]; const grades={}; let stuck=0; const seen={};
 for(let r=0;r<runs;r++){
   gStart(classId,scen,diff,1000+r);
   let n=0;
   while(!G.ended&&n<120){ n++;
     const sc=G.scene; const ok=sc.choices.map((c,i)=>[c,i]).filter(([c])=>gChoiceState(c).ok);
     if(!ok.length){stuck++;break;}
     seen[sc.id]=(seen[sc.id]||0)+1;
     let pick;
     if(strategy==="random") pick=ok[Math.floor(Math.random()*ok.length)][1];
     else if(strategy==="smart"){
       const m=G.meters; const score=c=>{const e=c.effects||{};if(e.ending)return -999;
         let v=(e.warmth||0)*(m.warmth<60?2.5:1)+(e.energy||0)*(m.energy<40?1.5:0.5)+(e.dry||0)*0.8+(e.morale||0)*(m.morale<35?1.5:0.4)-(e.suspicion||0)*(m.suspicion>50?1.5:0.5)+(e.wear?(e.wear==="all"?14:9):0)+(e.sleep?2:0)+(e.sleepBlock?(m.warmth>45?6:-2):0)+(e.lnt||0)*3;
         if(e.pitch==="woodland"||e.pitch==="hedge") v+=10; if(e.pitch==="hilltop") v-=10; if(e.setFlag==="awning"||e.setFlag==="quilted") v+=6; return v;};
       pick=ok.sort((a,b)=>score(b[0])-score(a[0]))[0][1]; }
     else { // greedy: best weighted sum for current weakest meter
       const m=G.meters; const score=c=>{const e=c.effects||{};if(e.ending)return -999;
         return (e.warmth||0)*(m.warmth<50?2:1)+(e.energy||0)*(m.energy<40?1.5:0.6)+(e.dry||0)*0.6+(e.morale||0)*(m.morale<35?1.5:0.6)-(e.suspicion||0)*(m.suspicion>50?1.5:0.6)+(e.wear?8:0)+(e.sleep?2:0);};
       pick=ok.sort((a,b)=>score(b[0])-score(a[0]))[0][1]; }
     gChoose(pick);
   }
   if(n>=120) stuck++;
   const k=G.ended?G.ended.kind:"none"; res[k]=(res[k]||0)+1; turns.push(n);
   Object.entries(G.result?G.result.grades:{}).forEach(([g,v])=>{grades[g]=grades[g]||{};grades[g][v]=(grades[g][v]||0)+1;});
 }
 return {res,avgTurns:Math.round(turns.reduce((a,b)=>a+b,0)/turns.length),stuck,grades,scenesSeen:Object.keys(seen).length};
}"""
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(); pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("http://localhost:8765/"); pg.evaluate("localStorage.clear()"); pg.reload(); pg.click("#wKeep")
    pg.evaluate("S.ui=S.ui||{}; save=()=>{}")  # don't hammer localStorage during bot runs
    for scen in ["towpath","storm","midsummer","dartmoor"]:
      print("==",scen)
      for cid in ["cls_winter","cls_bivvy","cls_hammock"]:
        for strat in ["smart","random"]:
            r=pg.evaluate(BOT,[cid,scen,"normal",strat,120])
            print(cid,strat,json.dumps(r["res"]),"turns",r["avgTurns"],"stuck",r["stuck"],"scenes",r["scenesSeen"])
            pass
    b.close()
print("ERRORS",errs[:5])
