# Çok İzli Zaman Çizelgesi

Cetvel, iz başlıkları (göz/kilit), renk kodlu klipler (video, ses dalgalı, metin, efekt), seçili klip sarı çerçeve ve turuncu oynatma kafası (--p).

**Kimlik:** `PLA-063` · **Kategori:** Yaratıcı Araçlar · **Katman:** advanced

**Ne zaman:** Video/ses kurgusu, animasyon, sunum zamanlaması, otomasyon akışı.

**Durumlar:** varsayılan, klip seçili, iz kilitli, iz gizli

**Sınıflar:** `pl-tl pl-tl__ruler pl-tl__ticks pl-tl__track pl-tl__head pl-tl__lane pl-clip pl-clip--video|audio|text|fx is-selected pl-playhead (--p)`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** role="grid"; klipler <button> + aria-label (ad, başlangıç, süre); ← → 1 kare, Shift ile 1 sn.

**Desen kaynağı:** Pinler 17, 21 — video/ses/metin izli kurgu zaman çizelgesi

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
