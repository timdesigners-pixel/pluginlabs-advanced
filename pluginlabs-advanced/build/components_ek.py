"""PluginLabs ek bileşenleri (PLC-080 …) — temel kataloğun SONUNA eklenir.

components.py'deki listeye sırayla eklendiği için mevcut PLC-001…079 kimlikleri
değişmez. Stiller assets/pl-components.css sonundaki "EK BİLEŞENLER" bölümündedir.
Noktalı/ızgara önizleme zemini kullanılmaz.
"""
from components import add
from icons import I

KAT = "Ek Bileşenler"

add(slug="system-gauge", ad="Sistem Kadranı", kategori=KAT, urun="tweakster",
    aciklama="Yüzde halkası + başlık + açıklama: CPU, bellek, disk gibi tek bir yükü özetler.",
    ne_zaman="Tweakster sistem optimizasyonu, Hub kaynak kullanımı; ekranda en fazla 3 kadran.",
    durumlar=["varsayılan", "uyarı (is-warning)", "kritik (is-danger)"],
    siniflar="pl-gauge pl-gauge__ring pl-gauge__title pl-gauge__sub is-warning is-danger",
    a11y="Halka role=\"meter\" + aria-valuenow/min/max ve aria-label taşır; yüzde metin olarak da yazılıdır.",
    html='''<div class="pl-gauge"><div class="pl-gauge__ring" style="--v:78" role="meter" aria-valuenow="78" aria-valuemin="0" aria-valuemax="100" aria-label="CPU ve bellek yükü">%78</div>
<div><b class="pl-gauge__title">CPU &amp; Bellek Yükü</b><span class="pl-gauge__sub">3 arka plan görevi aktif</span></div></div>
<div class="pl-gauge is-warning" style="margin-top:10px"><div class="pl-gauge__ring" style="--v:91" role="meter" aria-valuenow="91" aria-valuemin="0" aria-valuemax="100" aria-label="Disk doluluğu">%91</div>
<div><b class="pl-gauge__title">Disk Doluluğu</b><span class="pl-gauge__sub">Uyarı · 12 GB boş alan kaldı</span></div></div>''')

add(slug="voice-hud", ad="Sesli Komut Çubuğu", kategori=KAT, urun="mymind",
    aciklama="Bas-konuş sesli komut HUD'u: yüzen AI küresi, canlı ses dalgası, durum metni ve iptal kısayolu.",
    ne_zaman="MyMind sesli komutu dinlerken; ekranın altında ya da odaklı alanın üstünde yüzer.",
    durumlar=["dinliyor (is-live)", "duraklatıldı (hover)", "işleniyor", "sessiz"],
    siniflar="pl-voicehud pl-voicehud__orb pl-voicehud__wave pl-voicehud__label is-live",
    a11y="role=\"status\" + aria-live=\"polite\" yalnız durum değişince duyurur; dalga aria-hidden. Esc ile iptal edilir; hareket azaltma açıkken dalga durur.",
    html='''<div class="pl-voicehud is-live" role="status" aria-live="polite"><span class="pl-voicehud__orb" aria-hidden="true"></span>
<span class="pl-voicehud__wave" aria-hidden="true"><i style="--h:45;--d:0"></i><i style="--h:80;--d:1"></i><i style="--h:60;--d:2"></i><i style="--h:95;--d:3"></i><i style="--h:50;--d:4"></i></span>
<span class="pl-voicehud__label">Dinleniyor…</span><kbd class="pl-kbd">Esc</kbd></div>''')

add(slug="scrub-input", ad="Sayısal Sürgü Kutusu", kategori=KAT, urun="replicator",
    aciklama="Etiketi sürükleyerek değeri değiştiren X/Y/W/H/R özellik kutuları.",
    ne_zaman="Design Replicator ve görsel denetçilerde konum, boyut, köşe ve açı alanları.",
    durumlar=["varsayılan", "hover", "odak", "sürükleniyor", "devre dışı"],
    siniflar="pl-scrubgrid pl-scrubinput pl-scrubinput__label",
    a11y="Her kutu gerçek <input inputmode=\"decimal\"> ve <label> taşır; ok tuşları ±1, Shift+ok ±10 değiştirir.",
    html='''<div class="pl-scrubgrid">
<label class="pl-scrubinput"><span class="pl-scrubinput__label">W</span><input inputmode="decimal" value="1200" aria-label="Genişlik"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">H</span><input inputmode="decimal" value="760" aria-label="Yükseklik"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">R</span><input inputmode="decimal" value="14px" aria-label="Köşe yarıçapı"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">∠</span><input inputmode="decimal" value="0°" aria-label="Açı"></label>
</div>''')

add(slug="price-matrix", ad="Çoklu Mağaza Fiyat Matrisi", kategori=KAT, urun="wishlist",
    aciklama="Aynı ürünün mağazalar arası canlı fiyat karşılaştırması; en iyi fiyat altın vurguyla işaretlenir.",
    ne_zaman="MyWishlist ürün ayrıntısı, Leo Helper indirim karşılaştırması.",
    durumlar=["varsayılan", "en iyi (is-best)", "stokta yok", "yükleniyor"],
    siniflar="pl-pricematrix pl-pricematrix__row pl-pricematrix__store pl-pricematrix__best pl-pricematrix__price is-best",
    a11y="<ul> listesi; en iyi satır renge ek olarak \"En iyi\" metnini taşır. Fiyatlar sağa hizalı ve tabular.",
    html='''<ul class="pl-pricematrix" aria-label="Mağaza fiyatları">
<li class="pl-pricematrix__row is-best"><span class="pl-pricematrix__store">Trendyol</span><span class="pl-pricematrix__best">En iyi</span><span class="pl-pricematrix__price">1.249,90 ₺</span></li>
<li class="pl-pricematrix__row"><span class="pl-pricematrix__store">Hepsiburada</span><span class="pl-pricematrix__price">1.389,00 ₺</span></li>
<li class="pl-pricematrix__row"><span class="pl-pricematrix__store">Amazon</span><span class="pl-pricematrix__price">1.412,50 ₺</span></li>
</ul>''')

add(slug="glass-titlebar", ad="Cam Başlık ve Sekme Çubuğu", kategori=KAT, urun="mindpalace", span=2,
    aciklama="Pencere ışıkları, sabitlenmiş uygulama sekmeleri ve kısayol ipucu taşıyan buzlu cam başlık çubuğu.",
    ne_zaman="Arkasında görsel ya da gradyan olan pencerelerde (Mind Palace tuvali, medya ekranları). Düz zeminde mevcut pl-titlebar kullanılır.",
    durumlar=["varsayılan", "sekme hover", "aktif sekme (is-active)", "odak"],
    siniflar="pl-glassbar pl-glassbar__lights pl-glassbar__tabs pl-glassbar__tab pl-glassbar__end is-active",
    a11y="Sekmeler role=\"tablist\"/\"tab\" + aria-selected; pencere ışıkları aria-hidden, gerçek pencere düğmeleri ayrıca etiketlenir.",
    html='''<div style="padding:16px;border-radius:var(--pl-radius-xl);background:var(--pl-grad-aurora)">
<div class="pl-glassbar"><span class="pl-glassbar__lights" aria-hidden="true"><i></i><i></i><i></i></span>
<div class="pl-glassbar__tabs" role="tablist" aria-label="Açık uygulamalar"><button class="pl-glassbar__tab is-active" role="tab" aria-selected="true">Mind Palace</button><button class="pl-glassbar__tab" role="tab" aria-selected="false">Leo Akışı</button><button class="pl-glassbar__tab" role="tab" aria-selected="false">Notlar</button></div>
<span class="pl-glassbar__end"><kbd class="pl-kbd">Ctrl T</kbd></span></div></div>''')

add(slug="box-model", ad="Kutu Modeli", kategori=KAT, urun="replicator",
    aciklama="Seçili öğenin dış boşluk (margin), iç boşluk (padding) ve boyutunu iç içe kutularla gösterir.",
    ne_zaman="Görsel denetçi, Design Replicator öğe incelemesi.",
    durumlar=["varsayılan", "hover (değer düzenlenebilir)"],
    siniflar="pl-boxmodel pl-boxmodel__pad pl-boxmodel__size",
    a11y="role=\"img\" + değerleri okuyan aria-label; aynı değerler denetçide sayısal alan olarak da bulunur.",
    html='''<div class="pl-boxmodel" role="img" aria-label="Dış boşluk 16, iç boşluk 14 ve 16, boyut 380 × 560">Margin · 16
<div class="pl-boxmodel__pad">Padding · 14 × 16<span class="pl-boxmodel__size">380 × 560</span></div></div>''')

add(slug="token-list", ad="Bağlı Tokenlar", kategori=KAT, urun="replicator",
    aciklama="Seçili öğenin hangi tasarım tokenlarına bağlı olduğunu özellik → token çipi olarak listeler.",
    ne_zaman="Denetçi panelinde, sabit değer yerine token kullanımını görünür kılmak için.",
    durumlar=["varsayılan", "aksan tokenı (is-accent)", "bağsız (sabit değer)"],
    siniflar="pl-tokenlist pl-tokenlist__row pl-tokenchip is-accent",
    a11y="<dl> yapısı: özellik <dt>, token <dd>; çipler kopyalanabilir metin.",
    html='''<dl class="pl-tokenlist">
<div class="pl-tokenlist__row"><dt>Zemin</dt><dd><code class="pl-tokenchip">--pl-bg-2</code></dd></div>
<div class="pl-tokenlist__row"><dt>Vurgu</dt><dd><code class="pl-tokenchip is-accent">--pl-accent</code></dd></div>
<div class="pl-tokenlist__row"><dt>Köşe</dt><dd><code class="pl-tokenchip">--pl-radius-lg</code></dd></div>
</dl>''')

_HEAT = [20, 60, 85, 100, 30, 45, 90, 70, 25, 80, 95, 40, 65, 100, 35, 55, 88, 92, 60, 75, 30, 50, 100, 70, 20, 45, 85, 60]
add(slug="activity-heatmap", ad="Etkinlik Isı Haritası", kategori=KAT,
    aciklama="Günlük/saatlik yoğunluğu aksan renginin tonlarıyla gösteren kare ızgara.",
    ne_zaman="Denetçide etkileşim yoğunluğu, eklenti kullanım geçmişi, katkı takvimi.",
    durumlar=["varsayılan", "boş (veri yok)", "hover (değer ipucu)"],
    siniflar="pl-heatmap (--cols, hücrede --v: 0–100)",
    a11y="role=\"img\" + özet aria-label; ayrıntılı değerler tablo olarak da sunulur.",
    html='<div class="pl-heatmap" style="--cols:14" role="img" aria-label="Son 28 günlük etkinlik: en yoğun günler hafta ortası">'
         + "".join(f'<i style="--v:{v}"></i>' for v in _HEAT) + '</div>')

add(slug="inspector-panel-ek", ad="Denetçi Paneli (Ek)", kategori=KAT, urun="replicator",
    aciklama="Sayısal sürgü kutuları, kutu modeli, bağlı tokenlar ve ısı haritasını tek denetçi panelinde birleştirir.",
    ne_zaman="Design Replicator sağ paneli; mevcut pl-inspector'a dokunmadan hafif bir alternatif.",
    durumlar=["varsayılan", "öğe seçili değil (boş)", "çoklu seçim"],
    siniflar="pl-inspectpanel pl-inspectpanel__head pl-inspectpanel__sec + PLC-082 · 085 · 086 · 087",
    a11y="<aside aria-label>; bölüm başlıkları pl-label, her alan etiketli.",
    html='''<aside class="pl-inspectpanel" aria-label="Denetçi">
<div class="pl-inspectpanel__head"><span class="pl-label">Denetçi · Inspector</span><span class="pl-badge pl-badge--accent">Kart</span></div>
<div class="pl-scrubgrid">
<label class="pl-scrubinput"><span class="pl-scrubinput__label">X</span><input inputmode="decimal" value="240" aria-label="X konumu"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">Y</span><input inputmode="decimal" value="118" aria-label="Y konumu"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">W</span><input inputmode="decimal" value="380" aria-label="Genişlik"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">H</span><input inputmode="decimal" value="560" aria-label="Yükseklik"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">R</span><input inputmode="decimal" value="14px" aria-label="Köşe yarıçapı"></label>
<label class="pl-scrubinput"><span class="pl-scrubinput__label">%</span><input inputmode="decimal" value="100" aria-label="Opaklık"></label>
</div>
<div class="pl-boxmodel" role="img" aria-label="Dış boşluk 16, iç boşluk 14 ve 16, boyut 380 × 560">Margin · 16<div class="pl-boxmodel__pad">Padding · 14 × 16<span class="pl-boxmodel__size">380 × 560</span></div></div>
<div class="pl-inspectpanel__sec"><span class="pl-label">Bağlı tokenlar</span>
<dl class="pl-tokenlist"><div class="pl-tokenlist__row"><dt>Zemin</dt><dd><code class="pl-tokenchip">--pl-bg-2</code></dd></div><div class="pl-tokenlist__row"><dt>Vurgu</dt><dd><code class="pl-tokenchip is-accent">--pl-accent</code></dd></div><div class="pl-tokenlist__row"><dt>Köşe</dt><dd><code class="pl-tokenchip">--pl-radius-lg</code></dd></div></dl></div>
<div class="pl-inspectpanel__sec"><span class="pl-label">Etkinlik ısı haritası</span>
<div class="pl-heatmap" style="--cols:14" role="img" aria-label="Son 28 günlük etkinlik">''' + "".join(f'<i style="--v:{v}"></i>' for v in _HEAT) + '''</div></div>
</aside>''')
