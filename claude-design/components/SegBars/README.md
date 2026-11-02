# Segment Çubuk Grafik

Yatay çizgilerle bölünmüş (LED) çubuklar; tepe değerler amber.

**Kimlik:** `PLA-041` · **Kategori:** HUD & Endüstri · **Katman:** advanced

**Ne zaman:** Saatlik yük, frekans dağılımı, gerçek zamanlı yoğunluk.

**Sınıflar:** `pl-segbars > span (--v) .is-peak`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="hud" lang="tr">`

**Erişilebilirlik:** role="img" + özet aria-label; ham veri tabloda.

**Desen kaynağı:** Pinler 10, 13 — dijital segmentli ekolayzer çubukları

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
