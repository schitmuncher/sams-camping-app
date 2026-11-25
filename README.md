# Sam's Camp Kit Planner

A single-page camping kit planner: open `index.html` in any browser (phone or desktop). No install or internet needed, and your data is saved in the browser.

## What it does

- **Kit**: every item you own, sorted into categories, with quantity, weight each, seasons, rain/wind/bug ratings, R-values and research notes. Tap an item to edit it. **+ Add item** has quick-fill templates (jacket, beanie, boots…). Each item can be marked *weighed*, *worn*, *needs repair*, or put on the **wishlist** (with price and which item it replaces, so you can see the weight you'd save).
- **Classes**: build loadouts with how many of each item you take. Mark items as **Worn** so they don't count toward pack weight. It comes with three presets (Winter Tent, Stealth Bivvy, Summer Hammock).
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
- **Data**: export the kit list, the current class or the trip log (CSV or JSON), make a full backup and import it, and install the app.

## Install as an app

When it's opened from GitHub Pages, the planner can be installed to your home screen (Android Chrome: ⋮ → Add to Home screen; iPhone Safari: Share → Add to Home Screen). It then works offline; only the forecast needs signal.

## Hosting on GitHub Pages

Go to Settings → Pages → Source: *Deploy from a branch* → `main` / root. The app will then be live at `https://schitmuncher.github.io/sams-camping-app/`.

## Notes on the data

Weights and ratings were checked against retailer and manufacturer listings (November 2026). Items marked "est." in their research note have no published figure. Budget gear like the Coolzon bag and AKSOUL mat has no official EN/ISO temperature or R-value, so those numbers are estimates. Edit any item to put in your own measured values.
