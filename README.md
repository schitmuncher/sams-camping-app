# Sam's Camp Kit Planner

A single-page camping kit planner: open `index.html` in any browser (phone or desktop). No install or internet needed, and your data is saved in the browser.

## What it does

- **🤖 Add with AI** (Kit tab): copy a ready-made prompt into ChatGPT, Claude, Gemini or any AI chat, then tell it what you own. It looks up weights, sleeping-bag temperatures and mat R-values, rates rain/wind/bug protection on the app's scales, and sorts everything into the app's categories. The prompt lists the kit already in the app, so the AI won't add duplicates and can send *updates* (e.g. a weight you've measured). Paste its reply back in; you see a preview, likely duplicates are unticked, and nothing is added until you confirm (with undo).
- **🧭 Kit check** (Plan and Classes tabs): for the current conditions it lists missing essentials (shelter, bag, mat, rucksack, head torch, first aid, water bottle, waterproofs, a lighter if your stove has no igniter, warm hat on cold nights, map & compass, water treatment, and more). It also flags packed dead weight (e.g. gas with no stove, a lantern on a stealth trip) with a one-tap **− Remove**. It separates things you own but haven't packed (**+ Pack**) from things you don't own (**+ Wishlist**, with a typical weight). When even your best kit can't handle the forecast (too cold, too wet, too windy, wrong pegs, not enough gas), it suggests what to get and why. The bottom bar shows how many essentials are missing.
- **🥷 Stealth** (Plan tab): choose how hidden you need to be (not important / some / high). The current class gets a 0–100 stealth score from shelter profile (flat bivvy → raised hammock), the colours of your shelter, rucksack and clothing (camo → bright, set per item or guessed from the name), lantern and white-only head torch use, reflective trim and stove noise. You get the biggest improvements, a score breakdown and fieldcraft tips. High stealth makes auto-suggest prefer a bivvy and muted colours and leave the lantern at home.
- **🍲 Food**: tap *Plan meals with AI* for a prompt that includes your trip length, forecast, calorie target and packed cooking kit. Paste the AI's reply back to import a day-by-day meal plan with weight, calories, protein, cooking water and utensils per meal. The plan drives food weight and gas needed, checks you've packed the utensils it needs, adds a food section to the checklist, and can copy a shopping list or export CSV. You can also add meals by hand.
- **Your own kit**: first-time visitors choose between exploring the example kit (Sam's) or starting empty. **Data → Start fresh** clears everything on that device. Auto-suggest, warnings and the fuel planner work from item types and names, so they work with anyone's gear.

- **Kit**: every item you own, sorted into categories, with quantity, weight each, seasons, rain/wind/bug ratings, R-values and research notes. Tap an item to edit it. **+ Add item** has quick-fill templates (jacket, beanie, boots…). Each item can be marked *weighed*, *worn*, *needs repair*, or put on the **wishlist** (with price and which item it replaces, so you can see the weight you'd save).
- **Classes**: **💾 Save** your loadout (suggested classes stay as drafts until you save or discard them), or use the ⋯ menu to save a copy, rename, export or delete. Build loadouts with how many of each item you take. Mark items as **Worn** so they don't count toward pack weight. It comes with three presets (Winter Tent, Stealth Bivvy, Summer Hammock).
- **Pack**: a tick-off checklist for the active class, with a progress bar. You can print it or copy it as text.
- **Plan**:
  - **Route (GPX)**: import a GPX from HiiKER (or Komoot, AllTrails…). Shows distance, climb, an elevation profile and walking time per day (Naismith, slowed for heavy packs). If the hike was split into days, each day's end becomes a camp; otherwise camps are spaced evenly and can be moved to any waypoint. After a forecast it also shows the latest start time to pitch before sunset.
  - **Live forecast** for any place, or for every camp on your route at its own height, up to 16 days ahead (Open-Meteo, no key needed). Multi-night trips are planned for the worst night, with a night-by-night table.
  - **Overnight temperature chart** for the coldest night, with your comfort and limit lines, hours below comfort, and hours of darkness.
  - **✨ Suggest a class**: builds a loadout from the forecast. It picks the shelter, matches pegs to the ground, stacks mats to the R-value needed, adds layers until you're warm enough, and works out gas. A short list explains each choice.
  - **Heat-retention stack**: bag comfort temperature, minus layers and shelter, plus penalties for too little ground R-value, wind chill, damp air, and your personal calibration. It warns when a night drops below your bag's limit, and **Cheapest warmth to add** ranks unpacked layers and mats by °C per 100 g.
  - **Rain, wind and midge protection** compared against the conditions, plus warnings and tips.
  - **Fuel & water planner**: litres to boil and grams of gas needed (adjusted for wind and cold), compared with the gas you're carrying.
- **Trips**: log each night out with the actual low and how warm you slept. The app works out whether you sleep warmer or colder than its maths and applies that offset (you can turn it off).
- **Reports**: exporting a class (Classes ⋯ menu or Data tab) now includes a full report: conditions and darkness hours; weight breakdown; the warmth stack step by step with ground insulation and the verdict explained; rain/wind/bug protection and which item provides it; stealth factors and fixes; essentials; dead weight; things worth buying; warnings; fuel, food and route. Every item gets its role and justification. There's also a readable Markdown trip report, a richer CSV, and **🤖 Ask an AI to review it**, which copies the report with a review prompt for a second opinion.
- **Data**: export the kit list, the current class or the trip log (CSV or JSON), make a full backup and import it, and install the app.

## 🌑 Pitch Dark (Play tab)

A button-based text survival game played with a real loadout from the planner. Pick a class, a scenario and a difficulty. Scenarios: *Off the Towpath* (−1°C November night by the Hurleston canals), *Storm Night* (35 mph gusts and rain, so loose pitches can fail), *Midsummer Midges* (warm, still and buggy, where you need a midge net and can overheat), *Dartmoor Commons* (legal wild camp on the open moor) or this class's own Plan conditions. Then walk in, choose a pitch, race the sunset, and get through the night hour by hour.

- **Five meters:** 🔥 warmth, ⚡ energy, 💧 dry, 🙂 morale, 👁️ suspicion. Warmth drains each hour using the planner's own warmth maths (layers you've actually put on, mats, shelter, wind, damp) against the overnight temperature. Starting suspicion comes from the class's stealth score, and energy drain from pack weight.
- **Kit matters:** choices you can't make show 🔒 and what's missing (head torch, flask, metal pegs, lighter…). Wrong pegs on frozen ground, a flask at 3am, the parka laid over the bag rather than worn inside it: it all plays out.
- **No death:** nights end with dawn, walking home (always available at night), bailing out, being moved on, calling it, or exhaustion.
- **Debrief:** grades (warmth, sleep, stealth, Leave No Trace, weight), the turning point of the night, and **Night Notes** with one-tap fixes back in the planner (+ Pack, + Wishlist). You can log the run as a practice night (shown on Trips, never used for calibration), replay the same night, or copy the story.
- Red night theme during night scenes. Progress autosaves.
- **The night (v3):** "Settle down and sleep" runs in blocks of up to four hours, broken by whatever wakes you: cold, a full bladder, a flapping corner, footsteps. Awake, you choose between real trade-offs. Layers and snacks rustle (so suspicion rises if someone's near), a torch lights you up (red light much less), sit-ups warm you but cost energy, and the flask cools through the night. Some choices come back later: skip the wee, skip dinner, or pull the bag over your head and you'll pay for it hours on. False alarms hide their outcome (❔), so you never know if it's a fox or a person. Walking pace and pack weight matter on the way in, and walking out shows how long it'll take. The ending tells you what hurt most and what held up.
- **Feedback and record:** every choice shows its meter changes (🔥−6 ⚡+3). The debrief shows your best move. A 🏅 Record panel tracks 16 achievements, nights to dawn, and how the recurring locals (boater, farmer, dog walker, angler, ranger) feel about you. They remember you between nights.
- `tests/game_bot.py` plays hundreds of nights per loadout to check balance: on the towpath the Winter Tent always reaches dawn with sensible play, the Stealth Bivvy ~85% and the Summer Hammock never (by design). Storm and midsummer are survivable with any class played well; Dartmoor beats the hammock.

## Layout

Sections and categories fold away and remember whether you left them open. Each section header shows a one-line status (e.g. *Warmth: 2°C vs −1°C, too cold*), so you can see everything at a glance and open only what you need. In the kit check, tap any item to see what it is, why it matters and what to look for.

## Install as an app

Open **https://schitmuncher.github.io/sams-camping-app/** and tap **📲 Install** (top-right). On Android, Chrome and Edge this opens the browser's own install prompt. On iPhone, Samsung Internet and others it shows the exact taps for that browser. Once installed it runs full-screen, works offline (only the forecast needs signal), and the home-screen icon has shortcuts straight to the checklist, trip planning and your kit (long-press the icon).

## Hosting on GitHub Pages

Go to Settings → Pages → Source: *Deploy from a branch* → `main` / root. The app will then be live at `https://schitmuncher.github.io/sams-camping-app/`.

## Notes on the data

Weights and ratings were checked against retailer and manufacturer listings (November 2026). Items marked "est." in their research note have no published figure. Budget gear like the Coolzon bag and AKSOUL mat has no official EN/ISO temperature or R-value, so those numbers are estimates. Edit any item to put in your own measured values.
