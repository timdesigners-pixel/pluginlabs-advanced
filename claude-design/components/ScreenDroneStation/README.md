# Drone Yer İstasyonu

Kokpit yüzey: sol ray, büyük kamera akışı ve sağda cihaz durumu; altta mini harita, telemetri, joystick ve pusula.

**Kimlik:** `PLA-099` · **Kategori:** Ekran Şablonları · **Katman:** advanced

**Ne zaman:** Drone/robot kontrolü, uzaktan kamera, saha cihazı yönetimi.

**Sınıflar:** `pl-screen + pl-rail + pl-camfeed + pl-range + pl-telemetry + pl-dpad + pl-compass`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" data-pl-surface="cockpit" lang="tr">`

**Erişilebilirlik:** Kumanda düğmeleri klavye eşdeğerli; kritik pil uyarısı role="alert".

**Desen kaynağı:** Pin 18 — drone kumanda uygulaması: kamera, durum, harita, joystick, pusula

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
