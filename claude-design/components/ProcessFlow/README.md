# Proses Akış Şeması

SVG tabanlı tank–boru–vana şeması; akan hat kesik çizgi animasyonlu, tank doluluk seviyesi gösterilir.

**Kimlik:** `PLA-040` · **Kategori:** HUD & Endüstri · **Katman:** advanced

**Ne zaman:** Endüstriyel izleme, veri hattı (pipeline) görselleştirme, otomasyon akışları.

**Durumlar:** akış, vana kapalı (kırmızı), durdu (animasyon yok)

**Sınıflar:** `pl-process .p-pipe .p-flow .p-tank .p-level .p-valve.is-off`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** SVG role="img" + ayrıntılı aria-label; aynı durum tabloyla da verilir.

**Desen kaynağı:** Pin 29 — tank, boru ve vanalı SCADA proses ekranı

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
