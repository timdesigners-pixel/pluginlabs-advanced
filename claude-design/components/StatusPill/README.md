# Durum Pili

Canlı bağlantı/senkron durumu; nokta + metin.

**Kimlik:** `PLC-007` · **Kategori:** Temel · **Katman:** temel

**Ne zaman:** Telegram bağlantısı, MyMind sunucu durumu, senkron gibi sürekli durumlar.

**Durumlar:** online, syncing (nabız), warning, error, offline

**Sınıflar:** `pl-status pl-status--online|syncing|warning|error`

**Kapsayıcı:** `<div data-pl data-pl-theme="dark" lang="tr">`

**Erişilebilirlik:** Renk tek başına değil, metin her zaman yazılır; değişince aria-live="polite".

**Tüketiciden beklenen:** `components/bundle.css` yüklü olmalı; örnekteki HTML yapısı ve sınıf adları aynen korunur. İkonlar Lucide (1.75 px), satır içi SVG.
