# Durum Çubuğu

Pencerenin en altında 26px şerit: senkron, dal/proje, imleç konumu, kodlama, sürüm. Tamamen mono.

**Kimlik:** `PLA-010` · **Kategori:** Kabuk & Pencere · **Katman:** advanced

**Ne zaman:** Editörler ve uzun süre açık kalan masaüstü araçları.

**Durumlar:** normal, senkronlanıyor, hata (öğe kırmızı)

**Sınıflar:** `pl-statusbar pl-statusbar__item is-accent pl-statusbar__spacer`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** role="status" + aria-live="polite" yalnız değişen öğe için.

**Desen kaynağı:** Pinler 17, 21 — editörlerin alt bilgi şeridi

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
