/* Run with an existing Playwright installation; no downloads or visible browser. */
const { chromium } = require(process.env.PL_PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const out = path.join(__dirname, 'evidence', 'after');

(async () => {
  fs.mkdirSync(out, { recursive: true });
  const server = http.createServer((req, res) => {
    const relative = decodeURIComponent(new URL(req.url, 'http://localhost').pathname).replace(/^\/+/, '');
    const file = path.resolve(root, relative || 'vitrin/index.html');
    if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
    try {
      const mime = { '.html': 'text/html; charset=utf-8', '.webp': 'image/webp', '.png': 'image/png' };
      res.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream' });
      res.end(fs.readFileSync(file));
    } catch { res.writeHead(404).end(); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1440, height: 1100 }, deviceScaleFactor: 1, reducedMotion: 'reduce' });
    const errors = [], missing = [];
    page.on('pageerror', err => errors.push(err.message));
    page.on('response', res => { if (res.url().startsWith('http://127.0.0.1') && res.status() >= 400) missing.push({ url: res.url(), status: res.status() }); });
    await page.goto(`http://127.0.0.1:${server.address().port}/vitrin/index.html`, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    assert.equal(await page.locator('section.v-sec').count(), 33);
    assert.equal(await page.locator('#pin-8 .pl-s08-hex').count(), 6, 'IoT status overlays preserved');
    assert.equal(await page.locator('#pin-100 .pl-vitrin-track').count(), 5);
    assert.equal(await page.locator('#pin-18 .pl-s18-hud').count(), 1);
    assert.equal(await page.locator('#pin-18 .pl-s18-hist').count(), 1);
    assert.equal(await page.locator('#pin-14 .v-img-ph').evaluate(el => getComputedStyle(el).backgroundImage.includes('karakter-3b.webp')), true);
    const canonical = fs.readFileSync(path.join(root, 'pluginlabs-advanced/assets/pl-pin-ekranlari.html'), 'utf8');
    const actual = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
    assert.deepEqual([...actual.matchAll(/<pre>.*?<\/pre>/gs)].map(m => m[0]), [...canonical.matchAll(/<pre>.*?<\/pre>/gs)].map(m => m[0]), 'copyable canonical code unchanged');
    const files = [...new Set([...actual.matchAll(/img\/([a-z0-9-]+\.webp)/g)].map(m => m[1]))];
    for (const file of files) {
      const response = await page.request.get(`http://127.0.0.1:${server.address().port}/vitrin/img/${file}`);
      assert.equal(response.status(), 200, file);
    }
    const screens = [];
    for (const pin of [2, 6, 7, 8, 14, 18, 45, 100]) {
      const device = page.locator(`#pin-${pin} .pl-device`).first();
      await device.scrollIntoViewIfNeeded();
      await device.locator('img').evaluateAll(imgs => Promise.all(imgs.map(i => i.decode())));
      await device.screenshot({ path: path.join(out, `pin-${pin}.png`) });
      screens.push(await device.evaluate(el => ({ pin: el.closest('section').id, width: el.clientWidth, height: el.clientHeight, images: [...el.querySelectorAll('img')].map(i => ({ src: i.getAttribute('src'), alt: i.alt, loaded: i.complete && i.naturalWidth > 0 })) })));
    }
    await page.setViewportSize({ width: 820, height: 1100 });
    for (const pin of [2, 6, 8, 100]) {
      const section = page.locator(`#pin-${pin}`);
      await section.scrollIntoViewIfNeeded();
      await section.locator('.pl-device').screenshot({ path: path.join(out, `pin-${pin}-820.png`) });
    }
    await page.setViewportSize({ width: 1440, height: 1100 });
    await page.locator('.v-hero').scrollIntoViewIfNeeded();
    await page.screenshot({ path: path.join(out, 'vitrin-overview.png') });
    assert.deepEqual(errors, [], 'no page errors');
    assert.deepEqual(missing, [], 'no local HTTP errors');
    const result = { platform: process.platform, browser: await browser.version(), viewport: [1440, 1100], compactViewport: [820, 1100], screenCount: 33, verifiedAssets: files.length, copyableBlocksUnchanged: true, iotMarkers: 6, errors, missing, screens };
    fs.writeFileSync(path.join(out, 'verification.json'), JSON.stringify(result, null, 2) + '\n');
    console.log(JSON.stringify(result, null, 2));
  } finally { await browser.close(); await new Promise(resolve => server.close(resolve)); }
})().catch(err => { console.error(err); process.exitCode = 1; });
