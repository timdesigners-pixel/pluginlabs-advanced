# PluginLabs Advanced'i Claude Code'un VARSAYILAN tasarım sistemi yapar (tüm projeler, Windows).
# Kullanım: zip'i açtığın klasörde →  powershell -ExecutionPolicy Bypass -File kurulum\kisisel-kur.ps1
$ErrorActionPreference = "Stop"
$Here   = Split-Path -Parent $PSScriptRoot
$Src    = Join-Path $Here "pluginlabs-advanced"
$Claude = Join-Path $HOME ".claude"
$Skills = Join-Path $Claude "skills"
$Hedef  = Join-Path $Skills "pluginlabs-advanced"
$Tarih  = Get-Date -Format "dd.MM.yyyy"
$Arsiv  = Join-Path $Claude ("_arsiv\" + $Tarih)
New-Item -ItemType Directory -Force $Skills | Out-Null
foreach ($eski in @($Hedef, (Join-Path $Skills "pluginlabs-design"))) {
  if (Test-Path $eski) { New-Item -ItemType Directory -Force $Arsiv | Out-Null; Move-Item $eski (Join-Path $Arsiv ((Split-Path $eski -Leaf) + "-" + (Get-Date -Format HHmmss))); Write-Host "Arşivlendi: $eski" }
}
Copy-Item $Src $Hedef -Recurse
Write-Host "Skill kuruldu -> $Hedef"
$Md = Join-Path $Claude "CLAUDE.md"
$Blok = Get-Content (Join-Path $PSScriptRoot "kisisel-CLAUDE.md.parca") -Raw -Encoding UTF8
if ((Test-Path $Md) -and ((Get-Content $Md -Raw -Encoding UTF8) -match "PLUGINLABS-ADVANCED-VARSAYILAN")) {
  Write-Host "CLAUDE.md zaten ayarlı, dokunulmadı."
} else {
  if (Test-Path $Md) { New-Item -ItemType Directory -Force $Arsiv | Out-Null; Copy-Item $Md (Join-Path $Arsiv ("CLAUDE.md-" + (Get-Date -Format HHmmss))) }
  Add-Content -Path $Md -Value ("`r`n" + $Blok) -Encoding UTF8
  Write-Host "Varsayılan kuralı eklendi -> $Md"
}
Write-Host "Tamam. Claude Code'u yeniden başlat."
