#!/usr/bin/env bash
# PluginLabs Advanced'i Claude Code'un VARSAYILAN tasarım sistemi yapar (tüm projeler, macOS/Linux/WSL).
# Kullanım: zip'i açtığın klasörde →  bash kurulum/kisisel-kur.sh
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
CL="$HOME/.claude"; SK="$CL/skills"; HEDEF="$SK/pluginlabs-advanced"
AR="$CL/_arsiv/$(date +%d.%m.%Y)"
mkdir -p "$SK"
for ESKI in "$HEDEF" "$SK/pluginlabs-design"; do
  if [ -e "$ESKI" ] || [ -L "$ESKI" ]; then mkdir -p "$AR"; mv "$ESKI" "$AR/$(basename "$ESKI")-$(date +%H%M%S)"; echo "Arşivlendi: $ESKI"; fi
done
cp -R "$HERE/pluginlabs-advanced" "$HEDEF"; echo "Skill kuruldu -> $HEDEF"
MD="$CL/CLAUDE.md"
if [ -f "$MD" ] && grep -q "PLUGINLABS-ADVANCED-VARSAYILAN" "$MD"; then echo "CLAUDE.md zaten ayarlı, dokunulmadı."
else
  [ -f "$MD" ] && { mkdir -p "$AR"; cp "$MD" "$AR/CLAUDE.md-$(date +%H%M%S)"; }
  printf '\n' >> "$MD"; cat "$HERE/kurulum/kisisel-CLAUDE.md.parca" >> "$MD"; echo "Varsayılan kuralı eklendi -> $MD"
fi
echo "Tamam. Claude Code'u yeniden başlat."
