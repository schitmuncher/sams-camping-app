# Pitch Dark: game design

*A button-based text survival game played with your real camping kit, built into Camp Kit Planner as a **Play** mode.*

Status: design draft v2 (Nov 2026), with Gemini's creative input merged in (full notes in `docs/game-content/gemini-creative-notes.md`). **M1 built, M2 content added, M3 real map mode built (stage 1: map, GPX, site survey; stage 2 next: illustrated camp scene)** (Play tab): four scenarios (towpath, storm, midsummer, Dartmoor), ~85 storylets with persistent locals, midge, wind and overheating mechanics, achievements, meter-delta feedback. M1: engine, five meters, all phases, 50+ scenes (10 walk-in by Gemini), dynamic pitch/food/bed/dawn scenes, six endings, debrief with grades, turning point and Night Notes actions, practice-night logging, save/resume, red night theme, balancing bot.

---

## 1. The pitch

One night wild camping in the UK, told in short text scenes with tap-to-choose buttons. You play with a loadout from the planner, and the planner's own maths decides what happens: your warmth stack, ground insulation, shelter ratings, stealth score, pack weight and meal plan. Real kit makes you better at the game, and the game shows you what's missing from your real kit.

**Design pillars**
1. **Real kit, real consequences.** Every item that matters has an effect. No made-up loot.
2. **Readable in a minute.** A short scene, 2–4 buttons, and a visible change to your meters. One hand on a phone.
3. **Tense, not cruel.** Bad nights end in "you bailed and walked home", never death. A failed run still teaches something.
4. **Every run gives a real-world lesson** that links back to the planner.
5. **Works offline** in the same installed app.

---

## 1b. Creative direction (v2)

**Title: Pitch Dark.** *One night out, when the lights go off.* Gemini and I both picked it: two plain words, sets the mood, and a nod to pitching in the dark. *Off the Towpath* is kept in reserve as the canal scenario's name.

**Voice: dry and observational.** Calm, second person, slightly wry, never melodramatic. It should read like a real notebook entry, not a novel. The kit and meters carry the tension; the narrator just notices. Reference line:
> *03:12. The cold has found the seam between your mat and your hip, and your toes feel like old sausages. Your sleeping bag isn't magic; it's just holding onto whatever warmth you brought into it.*

**Emotional arc:** anticipation (dusk, giddy, every rustle) → exposure (pitching, cooling fast, being careful near boats) → the long middle (slow, sensory, every weakness in your kit shows) → **earned quiet** (frost, grey light on the water, you stayed out). A good ending feels *grounding, not triumphant*. A failed ending feels *matter-of-fact and human*: useful data, not a game-over screen.

### The place: Cheshire canal, November
Use these as the palette for ambient lines and storylet text (rotate them so no two nights read the same):
- **Sounds:** water slapping steel hulls, distant A51/A500 hum, a train across the plain, a rope or chain clinking on a moored boat, a moorhen splash, tawny owls, a church clock.
- **Smells:** wet clay, dead leaves, diesel and woodsmoke from a boat stove, frost.
- **Light:** no streetlights past the town edge; a lit porthole, a distant lane, starlight on black water.
- **Through the night:** dusk (hedges go black first) → deep night (everything narrows to your hood and breath) → pre-dawn (coldest, mist on the water, first boaters stir) → sunrise (frost on reeds, and you see how close the lane really was).

### Locals (recurring characters)
Five people, each with a **disposition** that persists across runs on this device: be considerate and they warm to you, be careless and they remember.

| Character | Personality | Goes well | Goes badly |
|---|---|---|---|
| **The liveaboard boater** | Gruff, practical, cares about noise and rubbish | A nod, a tip about a muddy stretch, maybe a hot water refill (rare) | You rattle pots near their boat → moved on |
| **The dog walker** | Brisk, local, observant | "Evening." Doesn't care if you're tucked away | Pitching on the towpath edge; the dog finds your snacks |
| **The farmer** | Protective of stock and gates | Honest, packed early, no trace = shrug | Livestock field, open gate, litter or fire → moved on |
| **The night angler** | Patient, cold-hardened kindred spirit | Quiet chat, morale ▲ | Torch across their swim |
| **The Canal & River Trust ranger** | Low-key rule-keeper, rarely out of hours | Zero trace, they barely register you | Blocking the towpath, fire, litter |

### Signature dilemmas (both options cost something)
1. **The 3am wee:** hold it (lose sleep and morale) or get out into the cold (warmth ▼, noise, cold feet).
2. **Torch vs night vision:** light up to find the dropped peg (suspicion ▲) or fumble in the dark (time, dryness, morale).
3. **Vent vs seal:** crack the hood (warmth ▼) or zip tight (condensation, dry ▼ by morning).
4. **Pitch fast vs hunt for better:** settle before dark, or walk on for better cover and ground while the light goes.
5. **Bail vs tough it out:** a **"Walk home" button is always available at night**. Using it early with low warmth is *the sensible call* and gets a fair ending ("an early commute"), not a fail screen.

### Set pieces to write first
Moored-boat stove smoke · late dog walker's torch sweep · frost on the hood · mystery splash · frozen peg · headlights striping the shelter through bare hedges · the condensation drip at 02:20 · badger/fox snuffling at your pack · lock gate creak across still water · the boggy pitch mistake · distant tractor · phone dying in the cold · **mist roll-in** (muffles road noise, turns the torch into a milky wall, suspicion ▼ but navigation ▼) · early runner at 06:45 · the tempting bail-out (a lane back to Nantwich).

**Quiet rewards** (rare, morale ▲): stars through bare branches · first sip from the flask · a robin at first light · frost sparkling on fence wire at sunrise · packing up without a sound.

### Kit with personality, not just stats
Text should call out each item's quirks: the parka is warm on a bench but bulky in the bivvy · the yellow dry bag is great for organising and terrible left in plain sight · a white-only head torch still works if you **shield it with your hand** (a choice: less light, less suspicion) · the foam mat doubles as a seat · the flask is a 3am promotion.

### Humour (sprinkle, one at a time)
The cows are judging you. · Ten minutes after you stop walking, your body remembers it's November. · Your sleeping bag doesn't generate heat; it just charges interest on whatever you brought into it. · "Stealth camping" mostly means trying not to cough like a Victorian orphan. · A hot drink at 3am feels like a promotion. · Your toes have officially filed a complaint. · Nobody cares how tactical your camo is if you're rattling a crisp packet at midnight. · Moored boats have windows; keep your voice down like you're in a library. · Walking home in the dark isn't defeat, it's just an early commute. · Turns out "off-grid" in Cheshire is still within earshot of a road.

### Night Notes (the big idea)
After every run, the debrief writes a short **Night Notes** entry. If you got cold, damp or spotted, it points at the real cause in your real loadout (warmth stack, R-value, pegs, colours) and offers one-tap fixes in the planner. It can also **log the run on the Trips tab as a "practice night"** (kept separate from real nights, so it never skews your warmth calibration). The game becomes a rehearsal before you walk out the door.

### More scenarios (from Gemini, added to §9)
High Ridge Frost (Pennine edge, winter wind) · Woodland Rain & Midge Dusk (late spring) · Wet Towpath & Heavy Dew (autumn) · Short-Day Micro-Camp (December, ~16 h of dark: patience and morale) · Post-Rain Mud & High Water (soft banks, keep dry layers dry).

---

## 2. What we're borrowing (and from where)

| Game | What it does well | What we take |
|---|---|---|
| **Fallen London / Sunless Sea** (Failbetter): "quality-based narrative" | Content is small **storylets** that show up depending on **qualities** (stats/items), and every choice changes qualities. That brings the story back to the same place and keeps it growable. | Our whole event system: storylets gated by stats, kit, weather and time. Easy to add more without breaking anything. |
| **Reigns** (Nerial) | A handful of meters. Simple choices nudge them up or down, and a meter hitting its end finishes the run. Arrows hint at which meters a choice affects. | 4 survival meters + 1 danger meter, effect hints on buttons (direction and size, not exact numbers), quick restarts. |
| **The Long Dark** (Hinterland) | Survival meters for warmth, fatigue, thirst and hunger. **Cold drains you fastest**, while hunger and fatigue drain slowly. Wind chill and clothing warmth stack. | Warmth as the dominant, fast-moving meter. Energy as the slow one. Wind chill through shelter. |
| **A Dark Room** (Doublespeak) | Starts with almost nothing on screen and reveals new mechanics as you go. Minimal UI, the imagination does the work. | Opening scene with one button. Meters and options appear as they become relevant. No pictures needed. |
| **The Oregon Trail** (MECC) | Turn-based travel, resource management and **random events** drawn from a table. The designer tuned event frequencies against real diaries. | Turn structure (walk → camp → night), event tables weighted by real conditions, and balancing by tuning frequencies. |
| **Lifeline** (3 Minute Games) | Text messages with two choices. Optional **real-time** waits make it feel like it's really happening. | Later: an optional "Live night" mode that plays along in real time on the night you're actually out (notifications). |

---

## 3. Core loop (one run ≈ 10–15 minutes, 30–40 choices)

```
PACK ─▶ WALK IN ─▶ FIND A PITCH ─▶ PITCH (race the sunset) ─▶ NIGHT (hour by hour) ─▶ DAWN ─▶ DEBRIEF
```

| Phase | Turn length | What happens |
|---|---|---|
| **Pack** | — | Choose a scenario and a loadout (planner class). The kit check speaks up as your inner voice. |
| **Walk in** | 30 min | Route segments (towpath, fields, lanes, woodland). Fatigue from pack weight and distance. Events: mud, stiles, showers, dog walkers, closed bridges, livestock. |
| **Find a pitch** | 1 choice | 3–4 candidate spots with visible trade-offs (wind, stealth, ground, flood risk, flatness). |
| **Pitch** | 15 min | Race to sunset. Peg type against ground, rigging the poncho or tarp, head torch or no head torch. |
| **Night** | 1 hour | The engine ticks the real overnight temperature curve. Storylets fire: cold wake-ups, condensation, wildlife, torchlight, wind, rain, needing a wee at 3am. |
| **Dawn** | 15 min | Pack up before people are about. Leave No Trace check. |
| **Debrief** | — | Grades, the turning point of the night, real-world lessons, and one tap to add fixes to the planner wishlist. |

---

## 4. Meters

Shown as five slim bars at the top, appearing as they become relevant (A Dark Room style).

| Meter | Starts from | Drains when | Restores with | At the extreme |
|---|---|---|---|---|
| 🔥 **Warmth** | 80 | Each night hour: drain ∝ (effective comfort − air temp), using the planner's `thermal()` with that hour's temperature. Getting wet multiplies it. | Adding layers, hot flask drink, eating, moving about, better pitch | **0 → "Bail out" ending** (walk home cold). Under 25 the text goes terse and shivery. |
| ⚡ **Energy** | 70 + meals | Walking: (pack kg ÷ 10) per 30 min plus climb. Cold also burns energy. | Food from the meal plan (kcal ÷ 100), sleep hours | 0 → "Exhausted" (forced to pitch badly or bail) |
| 💧 **Dry** | 100 | Rain beyond your shelter's rating, condensation, wet ground without groundsheet or bivvy, sweating in the parka | Towel, venting, dry socks, poncho | Under 30 doubles warmth drain |
| 🙂 **Morale** | 60 | Cold, cramped bivvy in 16 h of darkness, being spotted, broken kit | Hot drink, a good view, pitching well, sunrise, a red-light read, the stars | 0 → "Calling it a night" ending (go home) |
| 👁️ **Suspicion** (danger) | from the stealth score: 100 − score | Lights, noise, bright kit visible, pitching near paths, staying past 8am | Red light, packing bright kit away, moving pitch, leaving early | **100 → "Moved on" ending** (asked to leave, so pack up in the dark) |

Sleep isn't a meter. It's counted in hours and graded at the end. You only sleep through an hour when Warmth is above 40, Dry above 30 and nothing woke you.

**Effect hints on buttons** (Reigns style): small icons with ▲ or ▼, sized small or big, never exact numbers. *"Put on the parka"* 🔥▲ ⚡▼(small, it's heavy) 🙂▲.

---

## 5. How the planner drives the game

The game imports the active class (or any class) straight from the planner's saved data on the same device.

| Planner value | Game effect |
|---|---|
| `thermal()` effective comfort, limit, R stack | Warmth drain per hour. Below the limit, drain doubles. |
| Shelter rain/wind/bug ratings vs conditions | Whether rain, gust and midge storylets hurt you or just add flavour |
| Stealth score and factors | Starting Suspicion, plus which "spotted" storylets can fire (lantern glow, bright rucksack, white torch) |
| Pack weight | Energy drain per walking turn, and how many walk turns you need |
| Meal plan (kcal, hot or cold) | Food options in the menu, energy restored, whether you can make a hot drink |
| Items present | **Unlock or block actions** (see §6) |
| Item condition (worn/repair) | Chance of a kit failure storylet |
| Forecast / route (GPX) | Hourly temperatures, rain hours, gusts, sunset/sunrise, walk segments and distances |
| Darkness hours | Length of the night phase and morale drain in a bivvy |

---

## 6. Kit affordances (the fun part)

Each item can add buttons, block buttons or change outcomes. Matched by item kind and name, the same way the planner's kit check works, so it works for any user's kit.

| Kit | Unlocks | Without it |
|---|---|---|
| Head torch | Pitch after dark at normal speed; *read for a bit* | Pitching in the dark takes 2× the turns, with a chance of losing a peg |
| Red-light mode | Move about at night without raising Suspicion | White light: Suspicion ▲ each use |
| Lantern | Morale ▲ in camp | Suspicion ▲▲ if stealth matters |
| Y-pegs / spiral pegs | Pitch on frozen/hard or soft ground respectively | Wrong pegs: "pegs won't go in". Waste turns or pitch loose (gust storylet hurts) |
| Poncho / tarp | Rig an awning (frost off your face, sit up out of the rain); poncho also as rain gear | Condensation and rain hit Dry harder |
| Insulated flask | *Hot drink* without a stove (limited uses) | — |
| Stove + gas + lighter | *Make a hot drink / hot meal* | Stove with no lighter: "click… nothing" |
| Foam/foil mats | Ground insulation (already in Warmth); foam doubles as a seat | — |
| Repair kit | Fix the *mat puncture* storylet | Flat mat: R drops for the rest of the night |
| Trowel | Leave No Trace toilet; dawn LNT bonus | LNT penalty |
| Power bank (kept in bag) | Phone works for the map and the forecast check | In cold, the phone dies and you lose a navigation option |
| Spare socks | Dry ▲ | — |
| Hi-vis vest | Safe lane walking at dusk | — (but Suspicion ▲ if worn at camp) |
| Monocular | Scout a pitch: reveals hidden pitch details | Pitch info stays vague |
| Water filter | Refill from canal/stream | Ration water (Energy ▼) |

---

## 7. Storylets (event system)

Content is a list of **storylets**: small scenes with conditions, a short text, 2–4 choices, and results. This is quality-based narrative, so it's easy to add more, and each one is self-contained.

```json
{
  "id": "night_cold_wake",
  "phase": "night",
  "when": { "warmthBelow": 45, "hourBetween": [1, 5] },
  "weight": 3,
  "once": false,
  "text": "You wake shivering. It's {hour}. The {bag} is damp at the hood and your feet are numb.",
  "choices": [
    { "label": "Pull on the {warmestUnwornLayer}", "requires": { "unwornLayer": true },
      "effects": { "warmth": "+layer", "morale": 5 }, "result": "Better. Slowly." },
    { "label": "Drink from the flask", "requires": { "item": "insulated", "flaskUses": 1 },
      "effects": { "warmth": 12, "morale": 8, "flaskUses": -1 }, "result": "Hot tea at 3am is a religious experience." },
    { "label": "Eat something", "requires": { "snack": true },
      "effects": { "energy": "+snack", "warmth": 4 } },
    { "label": "Curl up and wait for dawn",
      "effects": { "warmth": -6, "morale": -8 }, "result": "The minutes crawl." }
  ]
}
```

- **Text templates** fill in real item names (`{bag}`, `{shelter}`, `{warmestUnwornLayer}`), the hour, weather and place names.
- **Selection:** each turn, collect the storylets whose conditions are met, then pick by weight (Oregon Trail-style table). Some storylets are *forced*, e.g. sunset arrives.
- **Weather-linked weights:** gusts → wind storylets, humidity → condensation, May–Sept → midges, near paths → dog walkers.
- **Seeded randomness:** every run has a seed, so it can be replayed, shared ("try my night"), and tested.

### Starter storylet list (MVP target ≈ 40)

**Walk in:** muddy towpath · stile with a heavy pack · sudden shower · friendly dog walker ("camping? in this?") · cows in the field · closed swing bridge detour · pub at dusk (temptation: morale ▲, time ▼) · getting dark early · fill water at a tap · blister forming (first aid)

**Finding a pitch:** woodland edge · hedge line · canal bank · hilltop · *scouting with the monocular* · "is this private land?"

**Pitching:** wrong pegs · rigging the awning · last light · dropped a peg in the dark · ground frozen solid · a puddle where your head would be

**Night:** cold wake-up · condensation drip · fox circling · owl (morale ▲) · torch sweeping the field · car headlights on the lane · gust pulls a peg · rain sets in · mat goes flat · need a wee at 3am · stars come out (morale ▲) · phone dying in the cold · frost on the bivvy · 16 hours of darkness is long (morale)

**Dawn:** frost everywhere · early dog walker · pack up wet kit · Leave No Trace check · sunrise (morale ▲▲)

---

## 8. Endings and grading

**Endings**
- 🌅 **Made it to dawn** (graded)
- 🥶 **Bailed out**: Warmth hit 0, so you packed up and walked home in the dark
- 🔦 **Moved on**: Suspicion hit 100, so you were asked to leave
- 😩 **Called it a night**: Morale hit 0
- 😵 **Exhausted**: Energy hit 0 on the walk

**Debrief screen**
- Grades A–E for **Warmth**, **Sleep hours**, **Stealth**, **Leave No Trace** and **Weight**
- **The turning point:** the single choice or event that changed the night most (biggest meter swing)
- **Real lessons**, generated from the run, e.g. *"Your warmth bottomed out at 3am. The cheapest fix in your kit is the Nantwich Town FC hat (+1°C, 90 g), and it was in your rucksack."*
- **Buttons:** *+ Pack* / *+ Wishlist* on each lesson (straight into the planner) · *Replay this seed* · *Try another class* · *Share result*

---

## 9. Scenarios

| # | Scenario | Feel | Uses |
|---|---|---|---|
| 1 (MVP) | **Off the Towpath: Hurleston canal, November** | Cold, damp, dark at 4pm, stealth-ish | Forecast-style preset (−1°C, 85% humidity) |
| 2 | **Summer midge woodland** | Warm, buggy, short night, hammock country | Bug and lightness balance |
| 3 | **Storm night** | Gusts 35 mph, heavy rain | Shelter ratings and peg choice under stress |
| 4 | **Dartmoor legal wild camp** | Open moor, no stealth pressure, navigation and exposure | Map & compass, wind |
| 5 | **Tonight's forecast** (daily) | Real Open-Meteo forecast for your location | Everything, different every day |
| 6 | **Your route** | Multi-night from a GPX (camps, days, sunset) | Planner route engine |

Difficulty: **Walk in the park** (meters drain at 0.6×, hints show exact numbers), **Wild camper** (normal), **Hardcore** (no hints, kit can fail, one save).

---

## 10. Screen layout (phone, buttons only)

```
┌──────────────────────────────┐
│ 🔥▓▓▓▓▓░░ ⚡▓▓▓▓░░ 💧▓▓▓▓▓▓    │  ← meters (appear as relevant)
│ 🙂▓▓▓░░░ 👁️▓░░░░░   02:00 −2°C│  ← time + temperature
├──────────────────────────────┤
│ You wake shivering. The      │
│ Coolzon is damp at the hood  │  ← scene text (2–4 short lines)
│ and your feet are numb.      │
├──────────────────────────────┤
│ [ Pull on the parka  🔥▲ ⚡▼ ]│
│ [ Drink from the flask 🔥▲🙂▲]│  ← 2–4 big buttons with hints
│ [ Curl up and wait   🔥▼ 🙂▼ ]│
├──────────────────────────────┤
│  🎒 Kit   📜 Log   ⚙️          │  ← inventory, story log, settings
└──────────────────────────────┘
```

- Same dark green look as the planner, optional retro terminal theme.
- **Red night theme** turns on automatically during night scenes (also good practice for stealth).
- **Kit** button shows your loadout, what's worn and what's used up.
- **Log** button shows the story so far, shareable as text.

---

## 11. Tech plan

- **Built into the app:** a new **🎮 Play** tab in Camp Kit Planner. It uses the planner's own functions directly (`thermal`, `protection`, `stealth`, `weights`, kit matching), so the game and planner can never disagree, and it works offline and installed like the rest of the app.
- **Content:** storylets kept as a JSON block (`STORYLETS`) in the app, with a separate data file if it grows large. The engine is a small self-contained module in the same page.
- **Links back:** debrief buttons call the planner directly. *+ Pack* adds an owned item to the class, *+ Wishlist* adds a suggested item, and *Open class* jumps to the Classes tab.
- **State:** `{seed, scenario, classSnapshot, time, phase, meters, flags, inventoryUses, log[]}`, autosaved to localStorage after every choice.
- **No dependencies, no build step**, matching the planner.
- **Balancing tool:** a headless "bot" that plays 1,000 nights per scenario with simple strategies (random, greedy-warmth, stealthy) and reports ending rates and average grades. Tune storylet weights until about 60–70% of runs with a sensible loadout reach dawn (Oregon Trail-style tuning).
- **Tests:** add game flows to the existing Playwright suite (start, choose, save/resume, each ending reachable).

---

## 12. Build milestones

| Milestone | Contents | Size |
|---|---|---|
| **M1: Playable night** | Engine, meters, phases, 1 scenario, ~25 storylets, 3 endings, basic debrief | 1 session |
| **M2: Kit matters** | Full affordance table, effect hints, Kit screen, item-named text, lessons and wishlist link | 1 session |
| **M3: Content and balance** | ~40+ storylets, balancing bot, difficulty modes, all 5 endings | 1 session |
| **M4: Real world** | "Tonight's forecast" daily scenario, GPX multi-night, share result | 1 session |
| **M5: Extras** | Achievements (e.g. *Ghost*: never above 10 Suspicion), Live night real-time mode, optional AI narrator that rewrites scene text in a consistent voice | later |

---

## 13. Open questions (decide during M1)

1. ~~Tone~~ → decided: dry and observational (§1b).
2. ~~Name~~ → decided: *Pitch Dark*.
3. **Death:** keep it non-lethal (bail-out endings)? *Recommended yes*: realistic for UK camping and fits pillar 3.
4. **How exact are the hints:** Reigns-style arrows by default, exact numbers on the easy setting.

---

## Sources

- Failbetter Games, *StoryNexus developer diary 2* (quality-based narrative and storylets)
- Emily Short, *Beyond Branching: quality-based and salience-based narrative structures*
- Hinterland, *The Long Dark: Condition and Character Status*; The Long Dark wiki (condition drain rates)
- PC Gamer and Wikipedia on *Reigns* (meters, binary choices)
- Mediacommons, *Lighting a Fire: A Dark Room*; Pocket Gamer, *The making of A Dark Room*
- R. Philip Bouchard, *Imagining the New Design* (The Oregon Trail)
- Game Analytics / Game Developer on *Lifeline* (real-time text adventure)
