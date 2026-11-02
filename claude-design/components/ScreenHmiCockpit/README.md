# Araç HMI Kokpit

Kokpit yüzey: üstte gösterge kümesi; altta navigasyon kartı, medya, iklim anahtarları ve menzil çubuğu.

**Kimlik:** `PLA-096` · **Kategori:** Ekran Şablonları · **Katman:** advanced

**Ne zaman:** RENTAKAR filo telemetrisi, araç simülasyonu, otomotiv HMI prototipleri.

**Sınıflar:** `pl-screen + pl-cluster + pl-turn + pl-player + pl-devtile + pl-range + pl-gear`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="cockpit" lang="tr">`

**Erişilebilirlik:** Sürüş sırasında etkileşim sınırlı; tüm hedefler ≥44px.

**Desen kaynağı:** Pinler 19, 30, 32, 35, 41 — araç içi dijital gösterge ve orta konsol

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
