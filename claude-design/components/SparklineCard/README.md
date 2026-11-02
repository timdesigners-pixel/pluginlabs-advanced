# Mini Grafik Kartı

Değer + son dönem eğilimini gösteren küçük çizgi grafik.

**Kimlik:** `PLC-040` · **Kategori:** Veri · **Katman:** temel

**Ne zaman:** Fiyat geçmişi, CPU kullanımı, günlük yakalanan kod sayısı.

**Sınıflar:** `pl-kpi + inline <svg> (stroke: var(--pl-accent))`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** SVG role="img" + aria-label ile özet ("30 günde %14 düşüş").

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
