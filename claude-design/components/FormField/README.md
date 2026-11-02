# Form Alanı (Etiket + Yardım + Hata)

Etiket, giriş, yardım ve hata metnini birleştiren sarmalayıcı.

**Kimlik:** `PLC-027` · **Kategori:** Form · **Katman:** temel

**Ne zaman:** Her form girişi bu sarmalayıcıyla kullanılır.

**Durumlar:** normal, hata (is-error)

**Sınıflar:** `pl-field pl-field__label pl-field__help is-error`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** Yardım/hata metni aria-describedby; hata durumunda aria-invalid="true".

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
