# Takvim Panosu

Saat sütunu + kişi/ekip sütunları; renk kodlu, süreye göre yüksekliği değişen etkinlik blokları (--h).

**Kimlik:** `PLA-044` · **Kategori:** Üretkenlik & İK · **Katman:** advanced

**Ne zaman:** Ekip planlama, kaynak takvimi, oda rezervasyonu.

**Durumlar:** varsayılan, etkinlik seçili, sürükleniyor, çakışma (uyarı kenarlığı)

**Sınıflar:** `pl-board (--cols) pl-board__colhead pl-board__time pl-board__cell pl-evt (--c, --h) pl-evt__foot`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** role="grid"; etkinlikler <button> ve aria-label="Ekip toplantısı, 09:00–10:00".

**Desen kaynağı:** Pin 11 — sütunlu ekip takvimi ve renkli etkinlik blokları

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
