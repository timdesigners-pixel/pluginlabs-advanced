# Uygulama Penceresi

Trafik ışıklı başlık çubuğu, 22px köşe ve derin gölgeli masaüstü penceresi; 'floating' varyantında iç panoların hepsi pencere içinde yüzer.

**Kimlik:** `PLA-001` · **Kategori:** Kabuk & Pencere · **Katman:** advanced

**Ne zaman:** Her masaüstü uygulamasının kök kabuğu; onboarding ve pazarlama görsellerinde cihaz çerçevesi.

**Durumlar:** odaklı, odaksız (başlık soluk), floating

**Sınıflar:** `pl-window pl-window--floating pl-window__bar pl-window__lights pl-window__title pl-window__body`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** Pencere kontrolleri <button aria-label>; Windows'ta sağda pl-winctl kullanılır.

**Desen kaynağı:** Pinler 5, 7, 11, 17, 18, 31, 39 — yuvarlak köşeli, yüzen masaüstü pencereleri

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
