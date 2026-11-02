# Gösterge Kümesi

İki çentikli kadran (hız ve şarj), ortada perspektifli yol şeridi, yön tarifi ve sürüş istatistikleri.

**Kimlik:** `PLA-071` · **Kategori:** Mobilite & Cihaz · **Katman:** advanced

**Ne zaman:** Araç/filo (RENTAKAR) telemetri ekranı, sürüş simülasyonu, cihaz performans paneli.

**Durumlar:** sürüş, park (P), düşük şarj (sağ kadran amber)

**Sınıflar:** `pl-cluster pl-dial pl-dial--right (--v) pl-dial__val pl-cluster__center pl-cluster__road pl-cluster__stats`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="cockpit" lang="tr">`

**Erişilebilirlik:** Kadranlar role="meter"; hız değeri aria-live değildir (sürekli değişir), istenince okunur.

**Desen kaynağı:** Pinler 30, 35, 41 — HMI dijital gösterge paneli (hız / batarya kadranları)

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
