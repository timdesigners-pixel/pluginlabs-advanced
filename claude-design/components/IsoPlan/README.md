# İzometrik Plan Görüntüleyici

CSS 3B dönüşümüyle izometrik kat; renk kodlu odalar, seçili oda ışıması, köşede görünüm araçları ve lejant. Gerçek 3B model yerine geçen hafif yer tutucu.

**Kimlik:** `PLA-034` · **Kategori:** Akıllı Ev & IoT · **Katman:** advanced

**Ne zaman:** Akıllı ev, emlak, tesis yönetimi; 3B model yüklenene kadar ya da düşük güç modunda.

**Durumlar:** varsayılan, oda seçili, 2D (dönüşüm kapalı)

**Sınıflar:** `pl-isoplan pl-isoplan__floor pl-isoplan__room (--c) pl-isoplan__room--wide is-active pl-isoplan__legend`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** Odalar <button aria-label>; aynı bilgi Kat Seçici Paneli listesiyle de sunulur.

**Desen kaynağı:** Pinler 0, 1, 3, 6, 8, 15 — izometrik ev / ofis / kat planı sahneleri

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
