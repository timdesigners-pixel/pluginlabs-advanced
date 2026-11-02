# HUD Çerçeve Paneli

Kesik köşeli (clip-path) panel, ince ızgara dokusu, camgöbeği başlık şeridi ve köşe braketleri.

**Kimlik:** `PLA-009` · **Kategori:** Kabuk & Pencere · **Katman:** advanced

**Ne zaman:** Komuta merkezi, fabrika/IoT izleme, güvenlik ve sağlık görselleştirme ekranları.

**Durumlar:** normal, uyarı (başlık amber), kritik (başlık kırmızı)

**Sınıflar:** `pl-hudframe pl-hudframe__title pl-hudframe__corner--tl|br`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="hud" lang="tr">`

**Erişilebilirlik:** Dekoratif köşeler aria-hidden; başlık gerçek <h3> olarak da verilebilir.

**Desen kaynağı:** Pinler 10, 13, 16, 20, 43 — köşesi kesik, ızgaralı komuta paneli

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
