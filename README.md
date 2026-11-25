# Sam's Camp Kit Planner

A single-page camping kit planner: open `index.html` in any browser (phone or desktop). No install or internet needed, and your data is saved in the browser.

## What it does

- **Kit**: every item you own, sorted into categories, with quantity, weight each, seasons, rain/wind/bug ratings, R-values and research notes. Tap an item to edit it, or use **+ Add item** to add your own gear with its weight and ratings.
- **Class builder**: build loadouts ("classes") with how many of each item you take. Mark items as **Worn** so they don't count toward pack weight. It comes with three presets (Winter Tent, Stealth Bivvy, Summer Hammock). You can create, duplicate, rename or delete classes.
- **Checklist**: a tick-off packing list for the active class, with a progress bar. You can print it or copy it as text.
- **Weather stack**: type in the forecast low and high, rain, wind, midges, ground type, number of nights, water and food. Then you get:
  - a **heat-retention stack**: your sleeping bag comfort temperature, minus each layer and shelter bonus, plus a penalty when your stacked mat R-value is too low for the night. The verdict is *too cold*, *borderline*, *good* or *too warm*.
  - **rain, wind and midge protection** compared against the conditions
  - warnings and tips (pegs for frozen or peaty ground, gas below 0°C, tarp in gales, and more)
- **Weights**: base, consumables (gas, water, food), worn and total, with a breakdown by category and a list of the heaviest items.
- **Export / import**: kit list (CSV or JSON), the current class (CSV or JSON), or a full backup. Import a backup, a class file or a kit list on another device.

## Hosting on GitHub Pages

Go to Settings → Pages → Source: *Deploy from a branch* → `main` / root. The app will then be live at `https://schitmuncher.github.io/sams-camping-app/`.

## Notes on the data

Weights and ratings were checked against retailer and manufacturer listings (November 2026). Items marked "est." in their research note have no published figure. Budget gear like the Coolzon bag and AKSOUL mat has no official EN/ISO temperature or R-value, so those numbers are estimates. Edit any item to put in your own measured values.
