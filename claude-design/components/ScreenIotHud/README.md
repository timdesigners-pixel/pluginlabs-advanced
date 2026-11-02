# IoT Komuta HUD

HUD yüzey: üst başlık şeridi, sol metrik ve dalga panelleri, ortada izometrik tesis ve sıcak noktalar, sağda halka göstergeler ve alarm tablosu, altta olay şeridi.

**Kimlik:** `PLA-094` · **Kategori:** Ekran Şablonları · **Katman:** advanced

**Ne zaman:** Fabrika/IoT izleme, güvenlik operasyon merkezi, sunucu çiftliği panosu.

**Sınıflar:** `pl-screen + pl-hudframe + pl-hudmetric + pl-wavemon + pl-isoplan + pl-hotspot + pl-hudrings + pl-hudtable + pl-filmtick`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="hud" lang="tr">`

**Erişilebilirlik:** Kritik alarmlar role="alert"; diğer güncellemeler polite.

**Desen kaynağı:** Pinler 8, 10, 13, 16, 20, 43 — fabrika / şehir komuta merkezi ekranları

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
