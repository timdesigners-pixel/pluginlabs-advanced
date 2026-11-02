# Bu klasörü GitHub'da GİZLİ "pluginlabs-advanced" reposu olarak yayınlar (GitHub CLI gerekir).
# Kullanım: repo klasöründe →  powershell -ExecutionPolicy Bypass -File kurulum\github-yayinla.ps1
$ErrorActionPreference = "Stop"
Set-Location (Split-Path -Parent $PSScriptRoot)
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { Write-Host "GitHub CLI yok: winget install GitHub.cli  →  gh auth login"; exit 1 }
gh auth status 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) { gh auth login }
gh repo create pluginlabs-advanced --private --source . --remote origin --push --description "PluginLabs Advanced tasarım sistemi"
Write-Host "Tamam."
