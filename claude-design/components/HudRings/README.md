# HUD Halka Göstergeleri

Konik dolgulu, kesik çizgili iç halkalı dairesel göstergeler; değer --v ile.

**Kimlik:** `PLA-037` · **Kategori:** HUD & Endüstri · **Katman:** advanced

**Ne zaman:** Birden fazla yüzdeyi yan yana karşılaştırmak (doluluk, sağlık, kapasite).

**Sınıflar:** `pl-hudrings pl-hudring pl-hudring__dial (--v, --c)`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="hud" lang="tr">`

**Erişilebilirlik:** Her kadran role="meter" + aria-valuenow.

**Desen kaynağı:** Pin 10 — alt kısımdaki üçlü dairesel göstergeler

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
