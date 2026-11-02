# Düğüm Grafiği

Noktalı tuval, giriş/çıkış portlu düğüm kartları ve bezier bağlantılar; canlı bağlantı aksan renkli ışıyan.

**Kimlik:** `PLA-066` · **Kategori:** Yaratıcı Araçlar · **Katman:** advanced

**Ne zaman:** AI iş akışı (MyMind), otomasyon, veri dönüştürme hattı.

**Durumlar:** varsayılan, düğüm seçili, çalışıyor (canlı bağlantı), hata (kırmızı başlık noktası)

**Sınıflar:** `pl-nodes pl-node (--x, --y) is-selected pl-node__head pl-node__body pl-node__port pl-node__port--out`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** Tuval role="application" + düğüm listesi alternatifi; Tab ile düğümler, Enter ile port bağlama.

**Desen kaynağı:** Pin 14 — AI karakter üretim akışındaki girdi/çıktı düğümleri

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
