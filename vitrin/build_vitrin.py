"""Pin ekranları sayfasının görselli vitrin sürümünü üretir.

Kaynak:  pluginlabs-advanced/assets/pl-pin-ekranlari.html  (build_pins.py çıktısı, dokunulmaz)
Çıktı:   vitrin/index.html  (GitHub Pages: /vitrin/)

Her ekrandaki `pl-sx-ph` yer tutucusunun zeminine, o ekrana uygun görsel
eklenir; asıl gradyan arkada yedek olarak kalır. "HTML'i kopyala" kod
blokları değişmez, yani kopyalanan HTML hâlâ kanonik yer tutucuyu taşır.

Çalıştırma:  python -I vitrin/build_vitrin.py
"""
import re
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
KAYNAK = KOK / "pluginlabs-advanced" / "assets" / "pl-pin-ekranlari.html"
CIKTI = KOK / "vitrin" / "index.html"
IMG = KOK / "vitrin" / "img"

# Ekran başına görsel sırası; yer tutucular bu listeden sırayla (gerekirse
# başa dönerek) görsel alır.
ESLEME = {
    "pin-1": ["rezidans"],
    "pin-2": ["noir-sokak", "fener-orman", "kordon-yuruyus", "saat-kulesi",
              "orman-otoyol", "siber-sokak", "sovalye-ejder", "viking"],
    "pin-4": ["espor-yayin"],
    "pin-5": ["arena-duello", "viking", "siber-sokak", "orman-otoyol",
              "synth-lotus", "viking", "arena-duello", "sovalye-ejder",
              "siber-sokak", "orman-otoyol", "siber-portre", "cam-dugum",
              "noir-sokak", "fener-orman"],
    "pin-6": ["akilli-salon"],
    "pin-7": ["arena-duello", "siber-sokak", "viking", "orman-otoyol", "sovalye-ejder"],
    "pin-14": ["siber-portre"],
    "pin-17": ["kurgu-sahil", "kordon-yuruyus", "drone-kordon", "kurgu-sahil", "saat-kulesi"],
    "pin-18": ["drone-kordon"],
    "pin-30": ["synth-lotus"],
    "pin-45": ["orman-otoyol", "viking", "sovalye-ejder", "arena-duello",
               "siber-sokak", "espor-yayin", "noir-sokak", "sovalye-ejder", "fener-orman"],
    "pin-70": ["rezidans", "noir-sokak", "akilli-salon", "saat-kulesi"],
    "pin-100": ["synth-lotus", "cam-dugum", "noir-sokak", "kordon-yuruyus",
                "siber-portre", "fener-orman", "synth-lotus", "cam-dugum"],
    "pin-140": ["kordon-yuruyus", "burger", "saat-kulesi", "moda-duvar",
                "drone-kordon", "akilli-salon", "fener-orman"],
    "pin-155": ["espor-yayin", "arena-duello", "siber-sokak", "orman-otoyol", "viking",
                "sovalye-ejder", "synth-lotus", "burger", "kordon-yuruyus",
                "cam-dugum", "noir-sokak"],
    "pin-189": ["tasarim-izometrik", "kurgu-sahil", "cam-dugum"],
}

PH = re.compile(r'<div class="pl-sx-ph([ "][^>]*)>')
SEC = re.compile(r'<section class="v-sec" id="(pin-\d+)"')

HERO = """<section class="v-hero v-hero--img"><span class="pl-badge pl-badge--accent">Görselli vitrin · v2.0.0</span><h1>Pin ekranları,<br>gerçek görsellerle</h1><p>Aynı 33 ekran; yer tutucuların yerinde bu kez gerçek görseller var. Yerleşim, ölçü ve komponentler kanonik sayfayla birebir aynıdır; kopyalanan HTML yine yer tutucuyu taşır. <a href="../pluginlabs-advanced/assets/pl-pin-ekranlari.html">Yer tutuculu sürüm</a> · <a href="../pluginlabs-advanced/assets/pl-galeri.html">Komponent galerisi</a></p></section>"""

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

    s = re.sub(r'<section class="v-hero">.*?</section>', lambda _: HERO, s, count=1, flags=re.S)
    s = s.replace("</style>", HERO_CSS + "</style>", 1)
    s = s.replace('href="pl-galeri.html"', 'href="../pluginlabs-advanced/assets/pl-galeri.html"')
    s = re.sub(r"<title>[^<]*</title>", "<title>PluginLabs Pin Ekranları · Görselli</title>", s, count=1)

    CIKTI.write_text(s, encoding="utf-8")
    print(f"{toplam} yer tutucuya görsel eklendi -> {CIKTI.relative_to(KOK)}")
    for pid, n in sayac.items():
        print(f"  {pid}: {n}")


if __name__ == "__main__":
    main()
