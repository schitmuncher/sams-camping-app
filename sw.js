// Offline cache for the Camp Kit Planner. Bump VERSION when app files change.
const VERSION = "camp-kit-v25";
const SHELL = ["./", "./index.html", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png"];
self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION && k !== TILES).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
const TILES = "camp-tiles", TILE_MAX = 600;
self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  // map tiles: cache-first so areas you've looked at still show offline (kept to the last ~600 tiles)
  if (/^tile\.(openstreetmap|opentopomap)\.org$/.test(url.hostname) && e.request.method === "GET") {
    e.respondWith(caches.open(TILES).then(c => c.match(e.request).then(hit => hit || fetch(e.request).then(res => {
      if (res.ok) { c.put(e.request, res.clone()); c.keys().then(k => { if (k.length > TILE_MAX) k.slice(0, k.length - TILE_MAX).forEach(r => c.delete(r)); }); }
      return res;
    }))));
    return;
  }
  if (url.origin !== location.origin || e.request.method !== "GET") return; // forecast API goes straight to network
  // network-first so updates arrive when online, cache fallback when offline
  e.respondWith(
    fetch(e.request).then(res => {
      const copy = res.clone();
      caches.open(VERSION).then(c => c.put(e.request, copy));
      return res;
    }).catch(() => caches.match(e.request).then(r => r || caches.match("./index.html")))
  );
});
