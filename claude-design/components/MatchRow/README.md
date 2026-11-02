# Maç Satırı + Oran Çipleri

Lig ikonu, iki takım, skor ve seçilebilir oran düğmeleri; seçili oran aksan dolgulu.

**Kimlik:** `PLA-022` · **Kategori:** Canlı Veri & Spor · **Katman:** advanced

**Ne zaman:** Fikstür listeleri, karşılaştırmalı seçim satırları, A/B seçenek listeleri.

**Durumlar:** varsayılan, oran seçili, kilitli (devre dışı)

**Sınıflar:** `pl-matchrow pl-matchrow__teams pl-matchrow__score pl-odds button.is-active`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="neon" lang="tr">`

**Erişilebilirlik:** Oran grubu role="radiogroup"; her düğme role="radio" + aria-checked.

**Desen kaynağı:** Pin 4 — maç listesi ve 1/X/2 oran düğmeleri

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
