# HUD Büyük Metrik

Rajdhani rakamlı, metin gölgesiyle ışıyan büyük değer; yeşil / amber / camgöbeği varyantları.

**Kimlik:** `PLA-035` · **Kategori:** HUD & Endüstri · **Katman:** advanced

**Ne zaman:** Komuta ekranında tek bakışta okunması gereken ana değerler.

**Durumlar:** normal (yeşil), uyarı (amber), bilgi (camgöbeği)

**Sınıflar:** `pl-hudmetric pl-hudmetric--amber|cyan pl-hudmetric__ic pl-hudmetric__val pl-hudmetric__lbl`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="hud" lang="tr">`

**Erişilebilirlik:** Renk anlamı etiket metninde de verilir ("Normal", "Uyarı").

**Desen kaynağı:** Pin 10 — '102.67 / 127.39' ışıyan büyük değerler

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
