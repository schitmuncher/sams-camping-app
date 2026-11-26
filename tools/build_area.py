"""Build an offline map area for Pitch Dark (the game in Sam's Camp Kit Planner).

Downloads OpenStreetMap features and elevation for a box, in small tiles so the public
servers don't time out, and saves one compact file: data/<name>.json. Commit that file
and the game loads the area instantly, offline, without asking the busy map servers.
Same idea as Protomaps PMTiles and Arnis's tile archive: bake the data once, host it statically.

Needs only Python 3 (no installs).
    python3 tools/build_area.py                      # Nantwich and about 5 km around
    python3 tools/build_area.py hurleston 53.08 -2.60 53.11 -2.55
"""
import json, os, sys, time, urllib.request, urllib.parse

args = sys.argv[1:] or ["nantwich", "53.030", "-2.610", "53.110", "-2.450"]
name, S, W, N, E = args[0], *map(float, args[1:5])
MIRRORS = ["https://overpass-api.de/api/interpreter", "https://overpass.private.coffee/api/interpreter",
           "https://maps.mail.ru/osm/tools/overpass/api/interpreter", "https://overpass.kumi.systems/api/interpreter"]
KEEP = {"natural", "landuse", "waterway", "highway", "barrier", "building", "leisure", "amenity", "man_made", "place", "name", "width"}

def query(s, w, n, e):
    return f"""[out:json][timeout:180][bbox:{s},{w},{n},{e}];(
way["natural"];relation["natural"~"^(wood|water|wetland|heath|scrub)$"];way["landuse"];relation["landuse"~"^(forest|farmland|meadow|grass)$"];
way["waterway"];way["highway"];way["barrier"~"^(hedge|wall|fence|retaining_wall)$"];way["building"];way["leisure"~"^(park|nature_reserve|garden|pitch)$"];
node["natural"="tree"];node["amenity"~"^(bench|pub|drinking_water|parking)$"];node["natural"~"^(peak|rock)$"];node["man_made"="survey_point"];node["place"];
);out geom qt;"""

def fetch(q):
    for attempt in range(10):
        url = MIRRORS[attempt % len(MIRRORS)]
        try:
            req = urllib.request.Request(url, data=urllib.parse.urlencode({"data": q}).encode(), headers={"User-Agent": "sams-camping-app area builder"})
            with urllib.request.urlopen(req, timeout=240) as r:
                return json.load(r)
        except Exception as ex:
            print(f"  retry {attempt + 1} ({url.split('/')[2]}): {ex}")
            time.sleep(8 + attempt * 4)
    sys.exit("All map servers failed. Try again later.")

els, T = {}, 4
for i in range(T):
    for j in range(T):
        s, n = S + (N - S) * i / T, S + (N - S) * (i + 1) / T
        w, e = W + (E - W) * j / T, W + (E - W) * (j + 1) / T
        print(f"Downloading piece {i * T + j + 1}/{T * T}…")
        for el in fetch(query(s, w, n, e))["elements"]:
            els[(el["type"], el["id"])] = el
        time.sleep(2)

r5 = lambda v: round(v, 5)
flat = lambda g: [x for p in g for x in (r5(p["lat"]), r5(p["lon"]))]
out = []
for (t, _), el in els.items():
    tags = {k: v for k, v in (el.get("tags") or {}).items() if k in KEEP}
    if t == "node":
        out.append({"t": "n", "la": r5(el["lat"]), "lo": r5(el["lon"]), "g": tags})
    elif t == "way" and el.get("geometry"):
        out.append({"t": "w", "g": tags, "c": flat(el["geometry"])})
    elif t == "relation":
        mem = [{"r": m.get("role", ""), "c": flat(m["geometry"])} for m in el.get("members", []) if m.get("type") == "way" and m.get("geometry")]
        if mem:
            out.append({"t": "r", "g": tags, "m": mem})

print("Downloading heights…")
NY, NX = 33, 41
pts = [(S + (N - S) * y / (NY - 1), W + (E - W) * x / (NX - 1)) for y in range(NY) for x in range(NX)]
elev = []
for k in range(0, len(pts), 100):
    chunk = pts[k:k + 100]
    url = "https://api.open-meteo.com/v1/elevation?latitude=" + ",".join(f"{a:.5f}" for a, _ in chunk) + "&longitude=" + ",".join(f"{b:.5f}" for _, b in chunk)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                elev += [round(v) for v in json.load(r)["elevation"]]
            break
        except Exception as ex:
            print("  heights retry:", ex); time.sleep(5)
    time.sleep(1)

os.makedirs("data", exist_ok=True)
path = f"data/{name}.json"
json.dump({"name": name, "bbox": [S, W, N, E], "grid": [NY, NX], "elev": elev, "els": out}, open(path, "w"), separators=(",", ":"))
print(f"Saved {path}: {len(out)} features, {os.path.getsize(path) // 1024} KB. Commit it to the repo.")
