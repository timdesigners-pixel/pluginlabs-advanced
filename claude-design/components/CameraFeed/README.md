# Kamera Akışı HUD

16:9 akış; köşelerde REC, çözünürlük, histogram, pozlama değerleri ve merkezde nişangâh.

**Kimlik:** `PLA-077` · **Kategori:** Mobilite & Cihaz · **Katman:** advanced

**Ne zaman:** Canlı kamera, güvenlik kamerası, ekran kaydı önizlemesi.

**Durumlar:** canlı, kayıt, sinyal zayıf

**Sınıflar:** `pl-camfeed pl-camfeed__tl|tr|bl|br pl-camfeed__rec pl-camfeed__hist`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** <video> için altyazı/açıklama; HUD değerleri ayrıca metin listesinde.

**Desen kaynağı:** Pin 18 — drone kamera görüntüsü üzerinde REC, histogram, mod bilgisi

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
