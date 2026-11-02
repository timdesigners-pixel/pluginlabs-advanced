# Poster Rafı

Başlık + 'Tümünü gör' + ok düğmeleri ile yatay kaydırılan raf; scroll-snap ile poster hizalama.

**Kimlik:** `PLA-013` · **Kategori:** Medya & Eğlence · **Katman:** advanced

**Ne zaman:** Kategori rafları, son görüntülenenler, öneriler.

**Durumlar:** varsayılan, başta (sol ok pasif), sonda (sağ ok pasif)

**Sınıflar:** `pl-shelf pl-shelf__head pl-shelf__title pl-scroll-x pl-poster`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** Raf <section aria-labelledby>; oklar aria-controls ile rafı gösterir; klavyede Tab posterler arası gezer.

**Desen kaynağı:** Pinler 2, 5, 27 — 'Only on…', 'Movies', 'Games with discounts' rafları

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
