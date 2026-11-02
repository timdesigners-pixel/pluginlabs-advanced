# PluginLabs Advanced'i ~/github altındaki tüm PluginLabs projelerinde varsayılan yapar (Windows PowerShell).
# Kullanım: powershell -ExecutionPolicy Bypass -File kurulum\repolara-kur.ps1 [-Kok C:\Users\pc\github]
param([string]$Kok = (Join-Path $HOME "github"))
$ErrorActionPreference = "Stop"
$Kurulum = $PSScriptRoot
$Src     = Join-Path (Split-Path -Parent $Kurulum) "pluginlabs-advanced"
$Tarih   = Get-Date -Format "dd.MM.yyyy"
$Enc     = New-Object System.Text.UTF8Encoding($false)
$Isaret  = "PLUGINLABS-ADVANCED-VARSAYILAN"
$BlokC   = [IO.File]::ReadAllText((Join-Path $Kurulum "repo-CLAUDE.md.parca"), $Enc)
$BlokA   = [IO.File]::ReadAllText((Join-Path $Kurulum "repo-AGENTS.md.parca"), $Enc)

# Codex için kişisel kopya (~/.agents/skills)
$AgSk = Join-Path $HOME ".agents\skills"
$AgHedef = Join-Path $AgSk "pluginlabs-advanced"
New-Item -ItemType Directory -Force $AgSk | Out-Null
if (Test-Path $AgHedef) { $a = Join-Path $HOME ".agents\_arsiv\$Tarih"; New-Item -ItemType Directory -Force $a | Out-Null; Move-Item $AgHedef (Join-Path $a ("pluginlabs-advanced-" + (Get-Date -Format HHmmss))) }
Copy-Item $Src $AgHedef -Recurse
Write-Host "Codex kişisel skill -> $AgHedef"

function PluginLabsMi($d) {
  foreach ($n in "CLAUDE.md","AGENTS.md","README.md") { $p = Join-Path $d $n; if ((Test-Path $p) -and (Select-String -Path $p -Pattern "pluginlabs" -Quiet)) { return $true } }
  return $false
}

function MdIsle($repo, $ad, $blok, $olustur) {
  $p = Join-Path $repo $ad
  if (Test-Path $p) {
    $t = [IO.File]::ReadAllText($p, $Enc)
    if ($t -match $Isaret) { return "$ad zaten ayarlı" }
    $a = Join-Path $repo "_arsiv\$Tarih"; New-Item -ItemType Directory -Force $a | Out-Null
    Copy-Item $p (Join-Path $a ($ad + "-" + (Get-Date -Format HHmmss)))
    $t = [regex]::Replace($t, "(skills|design-system)([/\\])pluginlabs-design", '$1$2pluginlabs-advanced')
    if (-not $t.EndsWith("`n")) { $t += "`n" }
    [IO.File]::WriteAllText($p, $t + "`n" + $blok, $Enc)
    return "$ad güncellendi"
  } elseif ($olustur) {
    [IO.File]::WriteAllText($p, $blok, $Enc)
    return "$ad oluşturuldu"
  }
  return "$ad yok, atlandı"
}

$Repolar = Get-ChildItem $Kok -Directory | Where-Object { (Test-Path (Join-Path $_.FullName ".git")) -and (PluginLabsMi $_.FullName) } |
  Sort-Object @{ Expression = { if ($_.Name -eq "PluginLabs") { 0 } else { 1 } } }, Name

foreach ($r in $Repolar) {
  $f = $r.FullName; $not = @()
  if (Test-Path (Join-Path $f "design-system\pluginlabs-design")) {
    & (Join-Path $Kurulum "kur.ps1") -Repo $f 6>$null | Out-Null
    $not += "skill repoya kuruldu"
  }
  $not += MdIsle $f "CLAUDE.md" $BlokC $true
  $not += MdIsle $f "AGENTS.md" $BlokA $false
  Write-Host ("{0,-26} {1}" -f $r.Name, ($not -join " · "))
}
Write-Host ("Tamam: {0} proje." -f $Repolar.Count)
