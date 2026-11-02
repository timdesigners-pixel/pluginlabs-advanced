# Hafta Gün Şeridi

Gün adı + mono gün numarası; seçili gün ters renk, bugün nokta işaretli.

**Kimlik:** `PLA-043` · **Kategori:** Üretkenlik & İK · **Katman:** advanced

**Ne zaman:** Takvim, ajanda, rezervasyon ekranlarının üstü.

**Durumlar:** varsayılan, bugün, seçili, devre dışı (geçmiş)

**Sınıflar:** `pl-daystrip > button.is-active.is-today`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** role="tablist"; her gün aria-label="Salı 16 Kasım".

**Desen kaynağı:** Pin 11 — üstte 'Mon 15 · Tue 16…' gün seçici

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
