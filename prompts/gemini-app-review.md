I'd like a frank, detailed review of a whole app I'm building with Claude: the camping planner AND the game built into it. Judge it as a real product someone would use on their phone before and during UK wild-camping trips. Cover how useful it is, how easy it is to use, whether it's accurate and trustworthy, what's missing, what's bloated, and whether the game earns its place. Be critical. I'd rather hear the problems now. Below is a full brief of how it works today.

# SAM'S CAMP KIT PLANNER: full app brief (November 2026)

## What it is
- A free phone web app (PWA) for planning UK wild camping and micro-adventures. Built for me (Sam, Nantwich, Cheshire), but it works for anyone's kit.
- One HTML file of about 620 KB: vanilla JavaScript, no framework, no account, no server. Hosted on GitHub Pages and installable to the home screen.
- Works offline after the first load. Only the forecast, maps and AI need signal.
- All data lives in the browser (localStorage), with export and backup. Nothing is uploaded anywhere.
- There's an automated test suite of about 190 checks covering the planner and the game.
- Eight tabs along the top: 🎒 Kit, 🧩 Classes, ✅ Pack, 🗺️ Plan, 🍲 Food, 🌑 Play, 📓 Trips, 💾 Data.
- First visit: you choose between exploring my example kit (50 items, 3 loadouts) or starting empty. **Data → Start fresh** wipes the device.
- Sections fold away and remember their state. Each section header shows a one-line status (for example "Warmth: 2°C vs −1°C, too cold"), so you can scan everything and open only what you need.

## 1. Kit tab (inventory)
- **Every item I own,** grouped into categories (Shelter & Rigging, Sleep & Thermal, Clothing, Packs & Storage, Cooking, Lighting, Water, Navigation, First Aid and so on).
- **Fields per item:** quantity, weight each, seasons, rain/wind/bug ratings on the app's own scales, sleeping-bag comfort and limit temperatures, mat R-value, colour (for stealth), and a research note.
- **Flags:** weighed (measured, not the listed weight), worn, needs repair, and wishlist. Wishlist items have a price and say which item they'd replace, so you can see the weight you'd save.
- **+ Add item** has quick-fill templates (jacket, beanie, boots and so on).
- **🤖 Add with AI:** copies a ready-made prompt for ChatGPT, Claude or Gemini.
  - You tell the AI what you own. It looks up weights, bag temperatures and R-values, rates the protection on the app's scales, and sorts everything into categories.
  - The prompt lists your existing kit, so the AI won't add duplicates and can send updates instead (for example a weight you've measured).
  - You paste its reply back in and see a preview. Likely duplicates are unticked. Nothing is added until you confirm, and there's undo.
- **My example data:** weights and ratings were checked against retailer listings. Budget items without official EN/ISO ratings (a Coolzon bag, an AKSOUL mat) are marked as estimates.

## 2. Classes tab (loadouts)
- A "class" is a named loadout, such as Winter Tent (exposed), Stealth Bivvy (spring/autumn) or Summer Hammock (woodland). It records how many of each item you take, and marks items as **Worn** so they don't count toward pack weight.
- **💾 Save;** the ⋯ menu has save a copy, rename, export and delete. Suggested classes stay as drafts until you save or discard them.
- **🧭 Kit check** (also on the Plan tab), for the current conditions:
  - **Missing essentials:** shelter, bag, mat, rucksack, head torch, first aid, water bottle, waterproofs, a lighter if the stove has no igniter, a warm hat on cold nights, map and compass, water treatment and more.
  - **Dead weight** you've packed (gas with no stove, a lantern on a stealth trip), with a one-tap − Remove.
  - Things you own but haven't packed get **+ Pack**. Things you don't own get **+ Wishlist** with a typical weight.
  - When even your best kit can't cope (too cold, too wet, too windy, wrong pegs, not enough gas), it says what to buy and why.
  - The bottom bar shows how many essentials are missing. Tap any item to see what it is, why it matters and what to look for.
- **Exporting a class** gives a full report:
  - conditions and darkness hours, weight breakdown, and the warmth stack step by step with the verdict explained
  - rain/wind/bug protection and which item provides it, plus stealth factors and fixes
  - essentials, dead weight, things worth buying, warnings, fuel, food and route
  - a role and justification for every item
  - formats: Markdown trip report and CSV, plus **🤖 Ask an AI to review it**, which copies the report with a review prompt.

## 3. Pack tab
- A tick-off checklist for the active class, with a progress bar. It includes a food section if you have a meal plan.
- You can print it or copy it as text.

## 4. Plan tab (the brain)
- **Route (GPX):**
  - Import from HiiKER, Komoot, AllTrails and so on. You get distance, climb, an elevation profile, and walking time per day (Naismith's rule, slowed for heavy packs).
  - If the GPX is split into days, each day's end becomes a camp. Otherwise camps are spaced evenly, and you can move them to any waypoint.
  - After a forecast, it shows the latest start time that still lets you pitch before sunset.
- **Live forecast:** for any place, or for every camp on the route at its own height, up to 16 days ahead (Open-Meteo, no key). Multi-night trips are planned for the worst night, with a night-by-night table.
- **Overnight temperature chart** for the coldest night: your comfort and limit lines, hours below comfort, and hours of darkness.
- **✨ Suggest a class:** builds a loadout from the forecast. It picks the shelter, matches pegs to the ground, stacks mats to the R-value needed, adds layers until you're warm enough, and works out the gas. A short list explains each choice.
- **Heat-retention stack (the warmth model):**
  - It starts from the bag's comfort temperature, takes off degrees for layers worn and the shelter, and adds penalties for too little ground R-value, wind chill and damp air.
  - It applies my personal calibration (see Trips).
  - It warns when a night drops below the bag's limit.
  - **Cheapest warmth to add** ranks unpacked layers and mats by °C gained per 100 g.
- **Rain, wind and midge protection** compared against the conditions, with warnings and tips.
- **🥷 Stealth:**
  - You choose how hidden you need to be: not important, some or high.
  - The class gets a 0–100 score built from:
    - shelter profile (flat bivvy through to raised hammock)
    - colours of the shelter, rucksack and clothing (camo through to bright, set per item or guessed from the name)
    - lantern use, a white-only head torch, reflective trim and stove noise
  - You get a breakdown, the biggest improvements and fieldcraft tips.
  - High stealth makes Suggest prefer a bivvy, pick muted colours and leave the lantern at home.
- **Fuel & water planner:** litres to boil and grams of gas needed (adjusted for wind and cold), compared with the gas you're carrying.

## 5. Food tab
- **Plan meals with AI:** copies a prompt with your trip length, forecast, calorie target and packed cooking kit.
- You paste the reply back to import a day-by-day plan: weight, calories, protein, cooking water and utensils per meal.
- The plan feeds food weight and gas needed, checks you've packed the utensils it needs, adds food to the checklist, and can copy a shopping list or export CSV.
- You can also add meals by hand.

## 6. Trips tab (log and calibration)
- You log each night out with the actual low and how warm you slept.
- The app works out whether you sleep warmer or colder than its maths predicts and applies that offset to future plans (you can switch it off).
- Practice nights from the game appear here too, but they're never used for calibration.

## 7. Data tab
- Export the kit list, the current class or the trip log as CSV or JSON.
- Full backup and restore, and install the app. On iPhone, Samsung Internet and others it shows the exact taps for that browser.
- Long-pressing the home-screen icon gives shortcuts to the checklist, trip planning and kit.

## 8. Play tab: "Pitch Dark" (a game played with your real kit)
I've sent a separate, detailed brief on the game. In short:
- **What it is:** a top-down pixel-art survival and stealth game (Kenney CC0 sprites) about wild camping without being found. You play with one of your real classes, and the warmth model is the planner's own maths.
- **Modes:**
  - a 7-mission campaign: Ray, an old boater at Hurleston near Nantwich, trains me for a January week on Dartmoor
  - free play at 4 generated locations (towpath, hill, river meadows, Dartmoor)
  - real map: tap anywhere in the UK and a 640 m playable map is built from real OpenStreetMap shapes, height, forecast, sunset and moon
  - hike mode: walk a real GPX route in compressed time, with pace, slopes, energy, feet, daylight and trail event cards; camp anywhere along it and carry on next day
  - a daily challenge, and the old text "classic" mode
- **A night:** walk in before sunset, read the pitch preview (Hidden, Shelter, Ground, Dry, frost hollow, peg hardness, Leave No Trace distance), pitch and turn the door away from the wind. Then do camp jobs (stash food, hide bright kit, rig an awning, cook, flask, layers, wee) and sleep through interruptions (cold, bladder, rain, flapping, noise, night decision cards). Finally, pack up and walk out after first light.
- **Stealth AI:** dog walkers (the dogs smell you), joggers, the farmer, a gamekeeper, teenagers, anglers and cars. Each has a sight cone and hearing, and an awareness meter fills as they notice you. If you're caught, there's a dialogue (honest, excuse, snack for the dog), and you may have to move on. Locals remember you between nights.
- **Wildlife:** owls, foxes stealing food, badgers, deer, hedgehogs, hares, glow-worms and more, plus twists like a full moon, hard frost or lambing season.
- **Progression:** 3 contracts a night, a 12-species photo album, 15 ranks, 9 perks, 16 badges and a journal.
- **The link back to real life:**
  - The morning report grades Warmth, Sleep, Stealth, Leave No Trace and Weight, and shows "How your kit did" (thermal margin at the coldest point).
  - Night Notes have buttons that pack missing kit into your real class.
  - A 🔒 "Missing from this class" list shows owned kit you didn't pack and can add with one tap.
  - You can log the night as a practice trip.
- **My feedback on the game so far:** early on it was "a multiple choice quiz", "empty", "too easy", "no real direction" and "map too small". I liked the farmer and the dog-walker encounters. Lots has been added since that I haven't tested properly yet.

## Known limits and decisions
- Single user, single device. There's no sync between phone and PC apart from export and import.
- The warmth model is a heuristic (bag rating ± layers, shelter, R-value, wind, damp, personal offset), not a physiological model.
- Ratings for budget kit are estimates.
- The AI features don't call an API. They copy a prompt for you to paste into any chatbot, then you paste the reply back. That keeps the app free and keyless, but it's fiddly.
- The real map in the game depends on free Overpass servers, which can be slow. A pre-built offline Nantwich area is planned.
- The UI is dense: lots of sections, chips and buttons on a small screen.
- Similar tools I know of: LighterPack, PackWizard, Hikerbrain, Packstack, HiiKER, Komoot, OS Maps. None of them combine kit, warmth maths, stealth and a game.

# What I want from you
1. **First impression:** who is this for, and would they actually use it? What's the single most useful thing in it, and what's the least?
2. **First 5 minutes:** walk through what a new user sees and does. Where would they get lost, confused or overwhelmed? How should onboarding work?
3. **Phone UX:** with 8 tabs, folding sections and status chips, what would you merge, move, hide or cut? Is "Plan" doing too much?
4. **Trust and accuracy:** is the warmth stack, stealth score, Naismith timing and fuel planner believable? Where could it give dangerous or misleading advice, and how should it show uncertainty?
5. **The AI copy-paste workflow:** is it good enough, or a dealbreaker? Better alternatives that stay free and need no account?
6. **Missing features** a UK wild camper would expect: for example legal and access info, water sources, sunrise and dark-sky info, kit sharing, trip checklists by type, weather alerts, emergency info, offline maps. Rank them by value.
7. **The game:** does it belong inside a planner app, or should it be separate? How could it make the planner better, and the planner make the game better, so each feeds the other?
8. **Top 10 changes** to the whole app, ranked by impact, each with a one-line reason. Also anything I should CUT.
9. **Comparison:** how does this compare with LighterPack, HiiKER and the others? What should I steal from them, specifically?

Please write plain prose and short lists. No code or JSON.
