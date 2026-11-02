# Alt Menülü Bağlam Menüsü

PLC-034 menüsünün genişletmesi: açık alt menü öğesi aksan dolgulu, yanında ikinci seviye menü.

**Kimlik:** `PLA-070` · **Kategori:** Yaratıcı Araçlar · **Katman:** advanced

**Ne zaman:** Editörlerde nesne sağ tık menüsü.

**Sınıflar:** `pl-ctxmenu pl-menu pl-menuitem is-open pl-ctxmenu__sub`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** role="menu"/"menuitem"; aria-haspopup + aria-expanded; → alt menüyü açar, ← kapatır.

**Desen kaynağı:** Pin 22 — sağ tık menüsü ve açılan alt menü

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
