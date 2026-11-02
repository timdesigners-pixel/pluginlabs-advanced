# Menzil / Batarya Çubuğu

İkon + segmentli dolum + mono menzil; düşük seviyede amber.

**Kimlik:** `PLA-074` · **Kategori:** Mobilite & Cihaz · **Katman:** advanced

**Ne zaman:** Batarya, depolama, kota, kalan süre.

**Durumlar:** normal, düşük (is-low)

**Sınıflar:** `pl-range is-low pl-range__bar > i.is-on`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="cockpit" lang="tr">`

**Erişilebilirlik:** role="meter" + aria-valuetext="600 km, yüzde 80".

**Desen kaynağı:** Pin 35 — alt köşede '600 km' segmentli batarya

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
