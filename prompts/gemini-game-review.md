I'd like a frank, detailed review of a game I'm making with Claude. Focus on FUN: what's engaging, what's boring or pointless, what's confusing, and what would make me want to keep playing night after night. Be critical. I'd rather hear the problems now. Below is a full brief of how it works today.

# PITCH DARK: game brief (November 2026)

## What it is
"Pitch Dark" is a single-player survival and stealth game about UK wild camping, built into my phone web app, "Sam's Camp Kit Planner" (a PWA on GitHub Pages, all in one HTML file, vanilla JavaScript plus canvas). The planner holds my real camping kit: items with weights, warmth ratings, colours, waterproofing and so on, grouped into "classes" (loadouts) such as Winter Tent, Stealth Bivvy and Summer Hammock. The game is played with those real loadouts, so what I carry decides how the night goes. It's also meant to be USEFUL: it teaches real skills and sends lessons back into my real kit lists.

Platform: a phone (portrait), touch controls, sessions of about 5 to 20 minutes. It's in the "Play" tab of the app.

## Modes
1. **Campaign: "Training for the Big One"** (7 missions). Story: Ray, an old liveaboard boater at Hurleston near Nantwich, laughs at my plan to do a week on Dartmoor in January, then trains me. Each mission has a brief, required goals (some fail you the moment they're broken), and a win line.
   1. First Night: Hurleston towpath in October. Pitch somewhere rated 60+ hidden and reach morning.
   2. Nobody Saw a Thing: lots of dog walkers. Get spotted once and you fail instantly.
   3. Hard Frost: −4°C. Warmth must never drop below 30 (instant fail) and you need 5 hours' sleep.
   4. Storm Hill: wind and rain. Pitch sheltered from the wind and finish with dryness above 40.
   5. Lambing Season: the farmer patrols with a lamp at night, on Hardcore. Don't get caught by him, and walk out within 45 minutes of sunrise.
   6. The Short Night: midsummer, midges, teenagers about. Stay unseen, sleep 4 hours and photograph an animal.
   7. The Big One: Dartmoor in January, −3°C, gales and sleet, on Hardcore. Warmth must stay above 25 and Leave No Trace must be A.
2. **Free play** at 4 built-in locations (generated maps): Off the Towpath (Hurleston canal, November), Storm Hill (Bickerton Hills, October), Midsummer River (Weaver meadows, June) and Dartmoor Commons (legal wild camping). They unlock by rank.
3. **Real map:** scroll a real OpenStreetMap of the UK and tap a spot. The game downloads the real features around it (woods, hedges, water, paths, roads, railways, buildings, farms, height) and builds a 640 m playable map from them, with the real forecast, sunset and moon phase for that date.
4. **Hike mode (GPX):** load a real route, for example from the HiiKER app. You walk it on the real map in compressed real time (about 1 game minute per real second, with a ⏩ button). You set the pace (Stroll, Steady or Push), and slopes slow you down (Naismith's rule). Energy, feet, warmth, thirst, hunger and dryness wear down, and daylight runs out. The map dims after sunset, there's an elevation profile, and waypoint names pop up as you pass them. About every 1.6 to 3.4 km a trail event card appears: a muddy stile with your pack weight, mud, cows with calves, a missing signpost, a blister, a pub, a water tap, a view, a rain shower, a loose dog, a farmer who might tip you off about a camp spot, hunger, a flask brew. Some choices are 🔒 locked unless your kit has the item (a map, first aid, spare socks, a waterproof). Tap ⛺ Camp anywhere and the detailed camp map loads from OpenStreetMap at that exact point. In the morning, "Carry on" resumes the route, so long routes become multi-night trips.
5. **Daily challenge:** the same seed for everyone that day. **Classic story mode:** the old text-and-buttons version, still available.

## The camp night (the core game)
- **View:** top-down pixel art (Kenney CC0 sprites: trees by season, bush hedgerows, tiled roofs, 4-direction walking people, tents), drawn over a painted tile world. Day fades to dusk colours, then real darkness. Torch beams are lit cones, plus headlights, lit house and boat windows, and a stove flame. There's rain, fog, frost (your footprints show), the aurora (rare), and shooting stars you can tap. Simple procedural sound: wind, rain, owls, barking, footsteps, a heartbeat when you're being noticed.
- **Clock:** you arrive about an hour before sunset at the map edge (or where your GPX enters). 1 real second is about 0.25 game minutes while active, ⏩ is about 1.2, and Sleep fast-forwards about 9 game minutes per second.
- **Controls:** tap the map to walk (A* pathfinding; hedges, buildings, water and railways block you). Buttons: 🔦 torch (off, white, or red if the kit has red light), 🤫 sneak (slower and quieter), 🫥 lie flat (very hard to see, can't move), ⛺ pitch here, 🎒 kit drawer, 📷 photo (appears when an animal is close and lit), walk out.
- **Pitch preview:** rates the spot for Hidden (line of sight from paths and roads), Shelter (wind and upwind blockers), Ground (comfort, slope) and Dry (near water or in a dip). It warns about frost hollows, frozen ground versus your peg type, being under 60 m from water (Leave No Trace), and whether there are hammock trees. You rotate the door against the wind. Pitch time depends on shelter type, darkness and torch, cold hands and peg hardness. Hammering pegs on hard ground makes noise. Pegs may end up loose and flap in gusts later.
- **Camp jobs (kit drawer):** stash the food (otherwise a fox raids it), hide bright kit, rig a poncho or tarp awning, vent the shelter, cook (needs stove and water; noisy, with a flame light), boil water for the flask, eat, drink, use the flask (cools over hours), put on or take off each real layer, wee (Leave No Trace penalty near water or camp), dry socks, towel, check the phone forecast (shows when rain and gusts arrive), charge the phone, a geocache hot/cold app, filter water. A 🔒 "Missing from this class" list shows useful kit I own but didn't pack, with a button that adds it to my real class in the planner.
- **Camp comfort (●○○○○):** points for hidden, out of the wind, flat, dry or awning, and camp sorted. Minus a point if the door faces the wind. It boosts sleep quality and morale (like Valheim's rested bonus).
- **Body model:** warmth uses the planner's real thermal model, built from what you're actually wearing plus your shelter, mats, the temperature curve, wind at your spot, rain and damp. You also have energy, dryness, morale, hunger (6 hours without food lowers body heat), thirst, bladder and sweat (walking hard in layers soaks you and chills you later). A body silhouette shows warm or cold head, core, hands and feet. Status icons, plus water, food, flask, phone and torch battery (phones die fast in the cold unless kept in the bag).
- **Sleep:** blocks that last until something wakes you: cold, a full bladder, rain, a flapping corner, noise nearby, a torch on the camp, first light, midges, or your own snoring (which is noise people can hear). Waking hands control back to you, and you tap Sleep again. Random night decisions (dialogue cards) also interrupt: cold feet (flask, layers or sit-ups), rain hitting the bag (rig the poncho or dry bag), lampers sweeping the field (lie still or reveal yourself), something at your pack, cramp from dehydration, the sky clearing (stop and watch the stars).
- **Stealth AI:** people walk real paths on schedules. Dog walkers (dogs off the lead smell you, more so downwind or with food out, and bark, which brings the owner), joggers with head torches, the farmer doing evening and dawn rounds (extra in lambing season), a gamekeeper with a powerful lamp (twist), teenagers at a bench in summer, anglers at dawn, drunk walkers from the pub (twist), cars with headlights on roads. Each person has a sight cone (drawn in daylight; torches narrow and lengthen it) and hearing. An awareness ring fills over them, and the screen edge pulses red. Your noise shows as white rings, other sounds as coloured rings, with edge arrows for off-screen sounds. A visibility gem shows Hidden, Visible, Exposed or Lit up (light × cover × stance × shelter colour and visibility from my real kit data). If spotted: they come over and you get a dialogue (be honest, make an excuse, offer the dog a snack, ask to stay, argue). Outcomes change "heat", and with landowners or keepers you may have to pack up and move 40+ tiles away within an hour or the night ends. Two sightings make the farmer come looking. Locals remember you between games (dog walker, farmer, boater, angler, ranger moods).
- **Wildlife and moments:** tawny owls (calls), barn owls at dusk, foxes (green eyes in the torch; steal unstashed food), badgers, roe deer at dawn (watch still for 3+ minutes), hedgehogs, brown hares, herons, bats at dusk, Dartmoor ponies, cattle (twist: curious, come to you), sheep, a kingfisher flash, glow-worms (June and July, torch off), the dawn chorus, sunrise, stargazing.
- **Twists per night:** full moon (brighter and riskier), hard frost, cattle, lambing season, a gamekeeper, owl territory, lots of dog walkers, a meteor shower, fog at dawn, a pub night.
- **Endings:** made it (pack up after first light and walk off the map edge), walked out, too cold (warmth hits about 4), exhausted, called it (morale), moved on, overslept (camp found after 9am), mission failed.

## Progression and goals
- **Short-term:** 3 random contracts per night: pick up N litter (litter sits by paths and benches and gets collected as you walk past), find the geocache, pitch 80+ hidden, don't get spotted, sleep 6 hours, keep warmth above 45, explore half the map (fog of war on the 🗺 map), find a perfect pitch (2 hidden best spots per map get revealed when you're near), be gone within 30 minutes of sunrise, cook after dark, photograph a specific animal, photograph 3 different animals.
- **Mid-term:** a wildlife photo album with 12 species, rated 1 to 3 stars (closer, better lit, standing still; a camera flash at night can spook animals). Unfound species show hints.
- **Long-term:** 15 ranks from "Car Camper" to "Pitch Dark Legend". XP comes from every night, even failed ones (stars, moments, contracts, photos, litter, exploration, missions, km hiked). Ranks unlock locations and give perk points for 9 perks: Soft Step, Night Eyes, Quick Pitch, Warm Blooded, Hedge Ghost, Smooth Talker, Deep Sleeper, Naturalist, Iron Bladder. There are 16 badges, a journal of nights, and a no-torch challenge (+30% XP). Difficulty settings: Gentle, Wild camper (normal), Hardcore.
- **Morning report:** a 1 to 5 star rating; grades for Warmth, Sleep, Stealth, Leave No Trace and Weight; a map of your route; moments seen; XP breakdown and rank bar; contract results; "How your kit did" (thermal margin at the coldest point); Night Notes with lessons and buttons to pack the missing kit into my real class; "Log as practice night" (adds it to my real trip history in the planner).

## What I (the player) have said so far
- The early text version felt like "a multiple choice quiz", soulless and pointless.
- After the graphical rebuild: "no motivation to play longer than a minute or two", it "feels empty", "too easy and quite boring", "no real direction".
- On the real map near my house: it "wasn't very realistic", and the map "feels way too small". Hikes need to feel long.
- I DID like the farmer, the dog walker conversations, and some of the encounters.
- Claude has since added the campaign, harder detection, the hike mode, a bigger 640 m map drawn from real shapes, night decision cards, Kenney pixel art, contracts, photography, ranks and perks. I haven't played much of that yet.

## Known limits
- One player, no multiplayer. Animals are hand-drawn shapes, not sprites.
- The real map depends on the free Overpass servers, which can be slow. A pre-built offline Nantwich area is planned.
- Tuned so careful play usually passes missions and careless play usually fails.

# What I want from you
1. **First impression:** would this be fun? Where exactly would a player get bored, and when (first minute, first night, third night)?
2. **The core loop:** is "walk, pitch, sleep through interruptions, walk out" strong enough? What's missing minute to minute? Is there enough meaningful choice while waiting for dawn?
3. **Stealth:** is it interesting or just a meter? Ideas for tension and clever play that suit quiet UK camping (no combat).
4. **Survival:** does the kit-driven body model create interesting decisions, or is it invisible bookkeeping?
5. **Hike mode:** how to make a long GPX hike feel long and eventful without being tedious on a phone.
6. **Direction and motivation:** campaign, contracts, album, ranks. Which will actually pull me back, and which are filler? What's the single best reason to play another night?
7. **Usefulness:** how to make it more genuinely useful for planning real trips with my real kit, while staying fun.
8. **Top 10 changes,** ranked by impact on fun, each with a one-line reason. Also anything I should CUT.
9. Name a few games (mobile or PC) whose specific mechanics I should borrow, and say exactly which mechanic.

Please write plain prose and short lists. No code or JSON.
