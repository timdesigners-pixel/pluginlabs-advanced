# Dalga Formu Monitörü

Sol değer + sağda ışıyan dalga çizgisi; her satır kendi renk kanalını (--c) kullanır.

**Kimlik:** `PLA-036` · **Kategori:** HUD & Endüstri · **Katman:** advanced

**Ne zaman:** Gerçek zamanlı sinyal: sağlık, ağ trafiği, CPU/GPU yükü, sensör akışı.

**Durumlar:** akış, donmuş (kayıt), sinyal yok

**Sınıflar:** `pl-wavemon pl-wavemon__row pl-wavemon__val`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="hud" lang="tr">`

**Erişilebilirlik:** SVG role="img" + aria-label="Nabız 85, sabit".

**Desen kaynağı:** Pin 10 — 85 / 76 / 25 değerli EKG çizgileri

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
