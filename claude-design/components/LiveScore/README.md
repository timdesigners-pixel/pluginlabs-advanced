# Canlı Maç Skor Kartı

CANLI göstergesi, iki takım arması, büyük mono skor, dakika ve hakimiyet çubuğu.

**Kimlik:** `PLA-021` · **Kategori:** Canlı Veri & Spor · **Katman:** advanced

**Ne zaman:** Canlı skor, turnuva, yarışma ve gerçek zamanlı karşılaştırma panelleri.

**Durumlar:** canlı, devre arası, bitti, başlamadı (saat gösterir)

**Sınıflar:** `pl-score pl-score__head pl-score__live pl-dot--live pl-score__teams pl-score__crest pl-score__vs pl-score__bar`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="neon" lang="tr">`

**Erişilebilirlik:** Skor değişimi aria-live="polite" ile duyurulur; CANLI yalnız renk değil metindir.

**Desen kaynağı:** Pin 4 — canlı turnuva skor kartı

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
