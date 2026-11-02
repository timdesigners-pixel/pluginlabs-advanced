# HUD Veri Tablosu

Mono, büyük harfli başlıklı, zebra çizgili tablo; durumlar çerçeveli HUD etiketleriyle.

**Kimlik:** `PLA-038` · **Kategori:** HUD & Endüstri · **Katman:** advanced

**Ne zaman:** Cihaz listesi, alarm günlüğü, sipariş/üretim kuyruğu.

**Durumlar:** normal, uyarı, hata

**Sınıflar:** `pl-hudtable pl-hudtag pl-hudtag--warn|err`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="hud" lang="tr">`

**Erişilebilirlik:** Gerçek <table> + <th scope>; durum metinle.

**Desen kaynağı:** Pinler 13, 16 — sağ paneldeki durum tabloları

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
