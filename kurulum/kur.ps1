# PluginLabs Advanced tasarım skill'ini bir repoya kurar / eşitler (Windows PowerShell).
# Kullanım: powershell -ExecutionPolicy Bypass -File kur.ps1 -Repo C:\Projeler\PluginLabs
param([string]$Repo = (Get-Location).Path)
$ErrorActionPreference = "Stop"
$Here  = Split-Path -Parent $PSScriptRoot
$Src   = Join-Path $Here "pluginlabs-advanced"
$Kanon = Join-Path $Repo "design-system\pluginlabs-advanced"
$Tarih = Get-Date -Format "dd.MM.yyyy"
function Arsivle($p){ if(Test-Path $p){ $a = Join-Path $Repo ("design-system\_arsiv\$Tarih\" + (Split-Path (Split-Path (Split-Path $p -Parent) -Parent) -Leaf)); New-Item -ItemType Directory -Force $a | Out-Null; Move-Item $p (Join-Path $a ("pluginlabs-advanced-" + (Get-Date -Format HHmmss))); Write-Host "Arşivlendi: $p" } }
New-Item -ItemType Directory -Force (Join-Path $Repo "design-system"),(Join-Path $Repo ".claude\skills"),(Join-Path $Repo ".agents\skills") | Out-Null
Arsivle $Kanon; Copy-Item $Src $Kanon -Recurse; Write-Host "Kanonik kaynak -> $Kanon"
foreach($h in @((Join-Path $Repo ".claude\skills\pluginlabs-advanced"),(Join-Path $Repo ".agents\skills\pluginlabs-advanced"))){ Arsivle $h; Copy-Item $Kanon $h -Recurse; Write-Host "Skill -> $h" }
foreach($e in @((Join-Path $Repo ".claude\skills\pluginlabs-design"),(Join-Path $Repo ".agents\skills\pluginlabs-design"))){ if(Test-Path $e){ $a = Join-Path $Repo "design-system\_arsiv\$Tarih\temel"; New-Item -ItemType Directory -Force $a | Out-Null; Move-Item $e (Join-Path $a ((Split-Path (Split-Path (Split-Path $e -Parent) -Parent) -Leaf) + "-pluginlabs-design-" + (Get-Date -Format HHmmss))); Write-Host "Temel skill arşivlendi: $e" } }
Write-Host "Tamam. AGENTS.md ve CLAUDE.md'ye kurulum\*.parca içeriğini ekleyin."
