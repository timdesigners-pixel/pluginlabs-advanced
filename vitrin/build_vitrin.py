"""Pin ekranları sayfasının görselli vitrin sürümünü üretir.

Kaynak:  pluginlabs-advanced/assets/pl-pin-ekranlari.html  (build_pins.py çıktısı, dokunulmaz)
Çıktı:   vitrin/index.html  (GitHub Pages: /vitrin/)

Her ekrandaki `pl-sx-ph` yer tutucusunun zeminine, o ekrana uygun görsel
eklenir; asıl gradyan arkada yedek olarak kalır. "HTML'i kopyala" kod
blokları değişmez, yani kopyalanan HTML hâlâ kanonik yer tutucuyu taşır.

Çalıştırma:  python -I vitrin/build_vitrin.py
"""
import re
from html import escape
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
KAYNAK = KOK / "pluginlabs-advanced" / "assets" / "pl-pin-ekranlari.html"
CIKTI = KOK / "vitrin" / "index.html"
IMG = KOK / "vitrin" / "img"

# Ekran başına görsel sırası; yer tutucular bu listeden sırayla (gerekirse
# başa dönerek) görsel alır.
ESLEME = {
    "pin-1": ["rezidans"],
    "pin-2": ["tv-saat-kulesi-v2", "noir-sokak", "fener-orman", "kordon-yuruyus",
              "moda-duvar", "avatar-buyuk", "viking", "siber-sokak"],
    "pin-4": ["espor-yayin"],
    "pin-5": ["arena-duello", "viking", "siber-sokak", "orman-otoyol",
              "synth-lotus", "viking", "arena-duello", "sovalye-ejder",
              "siber-sokak", "orman-otoyol", "siber-portre", "cam-dugum",
              "noir-sokak", "fener-orman"],
    "pin-6": ["akilli-salon"],
    "pin-7": ["arena-duello", "siber-sokak", "viking", "orman-otoyol", "orman-otoyol"],
    "pin-14": ["karakter-3b"],
    "pin-17": ["kurgu-sahil", "kordon-yuruyus", "drone-kordon", "kurgu-sahil", "saat-kulesi"],
    "pin-18": ["drone-kordon"],
    "pin-30": ["synth-lotus"],
    "pin-45": ["orman-otoyol", "viking", "sovalye-ejder", "arena-duello",
               "siber-sokak", "espor-yayin", "noir-sokak", "sovalye-ejder", "fener-orman"],
    "pin-70": ["rezidans", "noir-sokak", "akilli-salon", "saat-kulesi"],
    "pin-100": ["album-sicak-akiskan", "album-sicak-akiskan", "album-sisli-orman",
                "album-gece-yolculugu", "album-lofi-oda", "album-yildizli-dag",
                "album-gece-yolculugu", "album-gece-yolculugu"],
    "pin-140": ["kordon-yuruyus", "burger", "saat-kulesi", "moda-duvar",
                "drone-kordon", "akilli-salon", "fener-orman"],
    "pin-155": ["espor-yayin", "arena-duello", "siber-sokak", "orman-otoyol", "viking",
                "sovalye-ejder", "synth-lotus", "burger", "kordon-yuruyus",
                "cam-dugum", "noir-sokak"],
    "pin-189": ["tasarim-izometrik", "kurgu-sahil", "cam-dugum"],
}

PH = re.compile(r'<div class="pl-sx-ph([ "][^>]*)>')
SEC = re.compile(r'<section class="v-sec" id="(pin-\d+)"')

HERO = """<section class="v-hero v-hero--img"><span class="pl-badge pl-badge--accent">Görselli vitrin · v2.0.0</span><h1>Pin ekranları,<br>gerçek görsellerle</h1><p>Aynı 33 ekran; yer tutucuların ve çizim alanlarının yerinde bu kez gerçek görseller var. Yerleşim, ölçü ve komponentler kanonik sayfayla birebir aynıdır; kopyalanan HTML yine yer tutucuyu taşır. <a href="../pluginlabs-advanced/assets/pl-pin-ekranlari.html">Yer tutuculu sürüm</a> · <a href="../pluginlabs-advanced/assets/pl-galeri.html">Komponent galerisi</a></p></section>"""

HERO_CSS = """
.v-hero--img{position:relative;overflow:hidden;border-radius:28px;padding:56px 40px;min-height:300px;display:flex;flex-direction:column;justify-content:flex-end;gap:12px;background:linear-gradient(90deg,rgb(9 13 24 / .92) 0%,rgb(9 13 24 / .72) 45%,rgb(9 13 24 / .15) 100%),url(img/tasarim-izometrik.webp) center/cover no-repeat;box-shadow:var(--pl-shadow-xl)}
.v-hero--img h1{color:var(--pl-on-media)}
.v-hero--img p{color:rgb(255 255 255 / .82)}
.v-hero--img a{color:var(--pl-brand-2)}
.v-img-ph{background-size:cover!important;background-position:center!important;background-repeat:no-repeat!important}
.v-img-ph > svg{display:none}
.pl-s04-hero .v-img-ph::after{content:"";position:absolute;inset:0;background:var(--pl-scrim-left)}
@media (max-width:900px){.v-hero--img{padding:32px 20px}}
"""

# Yer tutucusu (pl-sx-ph) olmayan ekranlar: görsel, ekranın kendi çizim alanına
# CSS ile konur ve o alandaki SVG çizim gizlenir. Seçiciler #pin-N ile sınırlıdır.
SAHNE_CSS = """
#pin-9 .pl-s09-dna{background:url(img/dna-sarmal.webp) 50% 50%/cover no-repeat}
#pin-9 .pl-s09-dna svg[viewBox="0 0 420 560"]{visibility:hidden}
#pin-10 .pl-s10-c{background:url(img/noral-tarama.webp) 50% 30%/cover no-repeat;border-radius:var(--pl-radius-lg)}
#pin-10 .pl-s10-c > svg,#pin-10 .pl-s10-c > .pl-s10-lab{visibility:hidden}
#pin-26 .pl-s26-head{position:relative;overflow:hidden}
#pin-26 .pl-s26-head > *{position:relative;z-index:1}
#pin-26 .pl-s26-head::before{content:"";position:absolute;inset:0 0 0 auto;width:46%;background:url(img/klinik-doktor.webp) 50% 28%/cover no-repeat;-webkit-mask-image:linear-gradient(90deg,transparent,var(--pl-bg-0) 55%);mask-image:linear-gradient(90deg,transparent,var(--pl-bg-0) 55%)}
#pin-30 .pl-s30-nav{background:url(img/hmi-harita.webp) 50% 50%/cover no-repeat}
#pin-30 .pl-s30-nav > svg{visibility:hidden}
#pin-50 .pl-s50-viz{background:url(img/akciger.webp) 50% 50%/cover no-repeat;border-radius:var(--pl-radius-xl)}
#pin-50 .pl-s50-viz > svg{visibility:hidden}
#pin-50 .pl-s50-dark{background:linear-gradient(0deg,color-mix(in srgb,var(--pl-bg-0) 85%,transparent) 15%,transparent 75%),url(img/kalp.webp) 50% 40%/cover no-repeat}
#pin-70 .pl-s70-3d{background:url(img/guvenlik-kesit.webp) 50% 58%/cover no-repeat;border-radius:var(--pl-radius-lg)}
#pin-70 .pl-s70-3d > svg,#pin-70 .pl-s70-scene > .pl-hotspot{visibility:hidden}
#pin-83 .pl-s83-video{background:url(img/gorusme-ana.webp) 50% 30%/cover no-repeat}
#pin-83 .pl-s83-person,#pin-83 .pl-s83-hand{visibility:hidden}
#pin-83 .pl-s83-thumbs > span:nth-child(1) .pl-sx-face{background:url(img/gorusme-y1.webp) 50% 40%/cover no-repeat!important}
#pin-83 .pl-s83-thumbs > span:nth-child(2) .pl-sx-face{background:url(img/gorusme-y2.webp) 50% 40%/cover no-repeat!important}
#pin-83 .pl-s83-thumbs > span:nth-child(3) .pl-sx-face{background:url(img/gorusme-y3.webp) 50% 40%/cover no-repeat!important}
#pin-178 .pl-s178-big{background:linear-gradient(180deg,color-mix(in srgb,var(--pl-bg-0) 40%,transparent),color-mix(in srgb,var(--pl-bg-0) 72%,transparent)),url(img/hava-sehir.webp) 50% 40%/cover no-repeat}
#pin-22 .pl-s22-poster{background:linear-gradient(180deg,color-mix(in srgb,var(--pl-bg-0) 30%,transparent),transparent 45%,color-mix(in srgb,var(--pl-bg-0) 35%,transparent)),url(img/poster-sahil.webp) 50% 60%/cover no-repeat}
#pin-22 .pl-s22-poster svg > :not(text){visibility:hidden}
#pin-23 .pl-s23-grid > .pl-s23-card .img{background:50% 50%/cover no-repeat;border-radius:var(--pl-radius-md);overflow:hidden}
#pin-23 .pl-s23-grid > .pl-s23-card .img > svg{visibility:hidden}
#pin-23 .pl-s23-grid > .pl-s23-card:nth-child(1) .img{background-image:url(img/burger.webp)}
#pin-23 .pl-s23-grid > .pl-s23-card:nth-child(2) .img{background-image:url(img/yemek-poke.webp)}
#pin-23 .pl-s23-grid > .pl-s23-card:nth-child(3) .img{background-image:url(img/yemek-sezar.webp)}
#pin-23 .pl-s23-o > .pl-s23-it .img{background:50% 50%/cover no-repeat!important}
#pin-23 .pl-s23-o > .pl-s23-it:nth-child(5) .img{background-image:url(img/yemek-poke.webp)!important}
#pin-23 .pl-s23-o > .pl-s23-it:nth-child(6) .img,#pin-23 .pl-s23-o > .pl-s23-it:nth-child(7) .img{background-image:url(img/yemek-sezar.webp)!important}
#pin-39 .pl-s39-photo{background:linear-gradient(0deg,color-mix(in srgb,var(--pl-bg-0) 70%,transparent),transparent 45%),url(img/avatar-buyuk.webp) 50% 20%/cover no-repeat}
#pin-61 .pl-s61-house{background:url(img/villa.webp) 50% 55%/cover no-repeat;border-radius:var(--pl-radius-lg)}
#pin-61 .pl-s61-house > svg{visibility:hidden}
#pin-116 .pl-s116-hero{background:linear-gradient(90deg,color-mix(in srgb,var(--pl-bg-0) 92%,transparent) 30%,color-mix(in srgb,var(--pl-bg-0) 10%,transparent) 80%),url(img/sanat-holo-kure.webp) 85% 50%/cover no-repeat}
#pin-116 .pl-s116-hero::after{display:none}
#pin-100 .pl-s100-cover{background:linear-gradient(0deg,color-mix(in srgb,var(--pl-bg-0) 55%,transparent),transparent 55%),url(img/album-sicak-akiskan.webp) 50% 50%/cover no-repeat}
#pin-100 .pl-s100-hero{background:linear-gradient(180deg,color-mix(in srgb,var(--pl-bg-0) 35%,transparent),var(--pl-bg-0) 100%),url(img/album-sicak-akiskan.webp) 50% 40%/cover no-repeat}
#pin-6 .pl-s06-disc{background:url(img/album-gece-yolculugu.webp) 50% 50%/cover no-repeat}
#pin-7 .pl-s07-promo{background:linear-gradient(90deg,color-mix(in srgb,var(--pl-bg-0) 94%,transparent) 30%,color-mix(in srgb,var(--pl-bg-0) 20%,transparent) 70%),url(img/valoris-taktik-v2.webp) 70% 0%/cover no-repeat}
#pin-7 .pl-s07-promo > .pl-s07-char{visibility:hidden}
#pin-14 .pl-s14-char{background:url(img/karakter-3b.webp) 50% 30%/cover no-repeat;border-radius:var(--pl-radius-xl);box-shadow:var(--pl-shadow-float)}
#pin-14 .pl-s14-char > svg{visibility:hidden}
#pin-116 .pl-s116-cards > .pl-s116-c .art{background-size:cover!important;background-position:50% 50%!important}
#pin-116 .pl-s116-cards > .pl-s116-c:nth-child(1) .art{background-image:url(img/sanat-neon-geometri.webp)!important}
#pin-116 .pl-s116-cards > .pl-s116-c:nth-child(2) .art{background-image:url(img/sanat-sivi-gradyan.webp)!important}
#pin-116 .pl-s116-cards > .pl-s116-c:nth-child(3) .art{background-image:url(img/sanat-kristal-cicek.webp)!important}
"""

# Vitrin katmanı: kanonik ekranların çizimlerini/kod örneklerini değiştirmez.
GELISTIRME_CSS = """
@layer pl {
[data-pl] .pl-vitrin-scene{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;pointer-events:none}
#pin-2 [data-pl] .pl-vitrin-scene{object-fit:cover;object-position:70% center}
#pin-6 [data-pl] .pl-vitrin-scene,#pin-8 [data-pl] .pl-vitrin-scene{mask-image:linear-gradient(to right,transparent,var(--pl-bg-0) 8%,var(--pl-bg-0) 92%,transparent),linear-gradient(to bottom,transparent,var(--pl-bg-0) 8%,var(--pl-bg-0) 92%,transparent);mask-composite:intersect}
#pin-2 [data-pl] .pl-s02-bg > svg,#pin-6 [data-pl] .pl-s06-scene > svg,#pin-8 [data-pl] .pl-s08-3d > svg{visibility:hidden}
#pin-6 [data-pl] .pl-s06-sensor{z-index:1}
#pin-8 [data-pl] .pl-s08-hex{z-index:1}
#pin-7 [data-pl] .pl-s07-promo p{color:var(--pl-on-media)}
#pin-45 [data-pl] .pl-s45-g{background-size:cover;background-position:center;color:var(--pl-on-media)}
#pin-45 [data-pl] .pl-s45-g small{opacity:1}
#pin-45 [data-pl] .pl-s45-g:nth-child(1){background-image:var(--pl-scrim-bottom),url(img/fener-orman.webp)}
#pin-45 [data-pl] .pl-s45-g:nth-child(2){background-image:var(--pl-scrim-bottom),url(img/kategori-uzay-v2.webp)}
#pin-45 [data-pl] .pl-s45-g:nth-child(3){background-image:var(--pl-scrim-bottom),url(img/cam-dugum.webp)}
#pin-45 [data-pl] .pl-s45-g:nth-child(4){background-image:var(--pl-scrim-bottom),url(img/valoris-afis.webp)}
#pin-100 [data-pl] .pl-vitrin-track{float:left;width:var(--pl-space-8);height:var(--pl-space-8);margin-right:var(--pl-space-2);border-radius:var(--pl-radius-sm);object-fit:cover}
#pin-100 [data-pl] .pl-s100-now .v-img-ph{background-position:center!important}
}
"""

SAHNELER = {
    "pin-2": ("pl-s02-bg", "tv-saat-kulesi-v2", "İzmir Saat Kulesi çevresinde yağmurlu bir gecede geçen özgün film sahnesi", 1600, 900),
    "pin-6": ("pl-s06-scene", "akilli-villa-izometrik-v2", "Odaları görünen izometrik akıllı villa; sıcaklık ve nem göstergeleri ayrı kontrollerdir", 1448, 1086),
    "pin-8": ("pl-s08-3d", "iot-bina-izometrik-v2", "Katları ve cihaz odaları görünen izometrik ofis binası; cihaz durumları yan panelde listelenir", 1448, 1086),
}


def gelistir(s):
    """Yalnız canlı bölüm HTML'ine ekle; kaçışlı kod örneklerini koru."""
    for pid, (sinif, ad, alt, genislik, yukseklik) in SAHNELER.items():
        if not (IMG / f"{ad}.webp").is_file():
            raise SystemExit(f"Eksik sahne görseli: {ad}")
        acilis = f'<div class="{sinif}">'
        if s.count(acilis) != 1:
            raise SystemExit(f"Sahne hedefi değişmiş: {pid}/{sinif}")
        s = s.replace(acilis, acilis + f'<img class="pl-vitrin-scene" src="img/{ad}.webp" alt="{escape(alt, quote=True)}" loading="lazy" decoding="async" width="{genislik}" height="{yukseklik}">', 1)

    # Eski sis/uçurum maketi kamera görüntüsünü kapatıyordu; HUD ve histogram kalır.
    s, n = re.subn(r'(<div class="pl-s18-cam">.*?</div>)<div style="position:absolute;left:30%;top:40%;[^>]+></div>', r'\1', s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("Drone kamera yer tutucusu değişmiş")

    kapaklar = iter(["album-okyanus", "album-gece-yolculugu", "album-yildizli-dag", "album-sisli-orman", "album-lofi-oda"])
    def tablo(m):
        def satir(t):
            ad = next(kapaklar)
            return f'<td><img class="pl-vitrin-track" src="img/{ad}.webp" alt="" loading="lazy" decoding="async" width="32" height="32">' + t.group(1)
        yeni, adet = re.subn(r'<td>(<b>[^<]+</b>)', satir, m.group(0))
        if adet != 5:
            raise SystemExit(f"Müzik tablosu değişmiş: {adet} satır")
        return yeni
    s, n = re.subn(r'<table class="pl-s100-tb">.*?</table>', tablo, s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("Müzik tablosu bulunamadı")
    return s

# Soyut avatarlar (pl-sx-face): Gemini ile üretilmiş 16 portreden sırayla. Yalnız canlı
# HTML değişir; kopyalanabilir kod bloklarındaki kaçışlı HTML soyut avatarla kalır.
AVATARLAR = [f"avatar-{i:02d}" for i in range(1, 17)]
FACE = re.compile(r'<span class="pl-sx-face" style="([^"]*?)background:')

# Görsel değişince anlamı da değişen tek metin: pin 50'deki koyu kart artık kalp gösteriyor.
METIN = [
    ('<b>Osteoporoz</b><span style="opacity:.7">Kemik yoğunluğu taraması</span>',
     '<b>Kalp Sağlığı</b><span style="opacity:.7">Koroner akış taraması</span>'),
]


def main():
    s = KAYNAK.read_text(encoding="utf-8")
    eksik = [n for v in ESLEME.values() for n in v if not (IMG / f"{n}.webp").exists()]
    if eksik:
        raise SystemExit(f"Eksik görsel: {sorted(set(eksik))}")

    # Bölüm başlangıçlarını bul, her yer tutucuyu ait olduğu ekrana bağla.
    bas = [(m.start(), m.group(1)) for m in SEC.finditer(s)]
    sayac, parcalar, son, toplam = {}, [], 0, 0
    for m in PH.finditer(s):
        pid = next((p for b, p in reversed(bas) if b < m.start()), None)
        liste = ESLEME.get(pid)
        if not liste:
            continue
        i = sayac.get(pid, 0)
        sayac[pid] = i + 1
        ad = liste[i % len(liste)]
        attrs = m.group(1)
        if 'style="' in attrs:
            attrs = attrs.replace('style="background:', f'style="background:url(img/{ad}.webp), ', 1)
        else:
            attrs = attrs.rstrip('"') + f'" style="background-image:url(img/{ad}.webp)"'
        # attrs boşlukla (ek sınıf) ya da tırnakla (sınıf sonu) başlar; ikisi de doğrudan eklenebilir.
        yeni = f'<div class="pl-sx-ph v-img-ph{attrs}>'
        parcalar += [s[son:m.start()], yeni]
        son = m.end()
        toplam += 1
    s = "".join(parcalar) + s[son:]

    sayac_av = iter(range(10**6))
    def _av(m):
        ad = AVATARLAR[next(sayac_av) % len(AVATARLAR)]
        return f'<span class="pl-sx-face" style="{m.group(1)}background:url(img/{ad}.webp) 50% 30%/cover no-repeat, '
    s, n_av = FACE.subn(_av, s)
    eksik = [a for a in AVATARLAR if not (IMG / f"{a}.webp").exists()]
    if eksik:
        raise SystemExit(f"Eksik avatar: {eksik}")

    s = re.sub(r'<section class="v-hero">.*?</section>', lambda _: HERO, s, count=1, flags=re.S)
    sahne_img = set(re.findall(r"img/([a-z0-9-]+)\.webp", SAHNE_CSS))
    eksik = sorted(n for n in sahne_img if not (IMG / f"{n}.webp").exists())
    if eksik:
        raise SystemExit(f"Eksik sahne görseli: {eksik}")
    for eski, yeni in METIN:
        if s.count(eski) != 1:
            raise SystemExit(f"Metin bulunamadı ya da birden fazla: {eski[:40]}…")
        s = s.replace(eski, yeni)
    s = gelistir(s)
    s = s.replace("</style>", HERO_CSS + SAHNE_CSS + GELISTIRME_CSS + "</style>", 1)
    s = s.replace('href="pl-galeri.html"', 'href="../pluginlabs-advanced/assets/pl-galeri.html"')
    s = re.sub(r"<title>[^<]*</title>", "<title>PluginLabs Pin Ekranları · Görselli</title>", s, count=1)

    # CSS, img ve sahne dahil tüm yerel görsel referanslarını doğrula.
    eksik = sorted({n for n in re.findall(r'img/([a-z0-9-]+)\.webp', s) if not (IMG / f"{n}.webp").is_file()})
    if eksik:
        raise SystemExit(f"Eksik vitrin görselleri: {eksik}")
    CIKTI.write_text(s, encoding="utf-8")
    print(f"{toplam} yer tutucuya görsel, {n_av} avatara portre eklendi -> {CIKTI.relative_to(KOK)}")
    for pid, n in sayac.items():
        print(f"  {pid}: {n}")


if __name__ == "__main__":
    main()
