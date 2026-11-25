# Tests

End-to-end browser tests (Playwright, Python). They cover every tab: kit editing, AI import, classes, checklist, forecast (mocked), GPX routes, warmth/stealth/kit check, suggestions, food, trips, export/import/reset, offline/PWA, a 350-item kit and phone/desktop layouts.

```
pip install playwright && playwright install chromium
python3 -m http.server 8765   # from the repo root, in another terminal
cd tests && python3 suite.py
```

Edit the `executable_path` in `suite.py` (or remove it) to use Playwright's own Chromium.
