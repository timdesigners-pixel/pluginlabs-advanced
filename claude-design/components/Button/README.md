# Buton

Birincil eylem tetikleyicisi. Beş varyant, üç boyut.

**Kimlik:** `PLC-001` · **Kategori:** Temel · **Katman:** temel

**Ne zaman:** Ekranda tek bir birincil buton olur; diğerleri secondary/ghost.

**Durumlar:** varsayılan, hover, odak, basılı, devre dışı, yükleniyor

**Sınıflar:** `pl-btn pl-btn--primary|secondary|ghost|danger|gradient pl-btn--sm|lg pl-btn--block is-loading`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** <button> kullan; yalnız ikonlu ise aria-label zorunlu. Yükleniyorken aria-busy="true".

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
