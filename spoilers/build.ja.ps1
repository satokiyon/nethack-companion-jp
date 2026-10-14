# NetHack Companion 日本語版 ビルドスクリプト (PowerShell ラッパー)
param(
    [switch]$SkipPdf
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
$PyScript = Join-Path $RootDir "tools\build_ja.py"

if ($SkipPdf) {
    python $PyScript --skip-pdf
} else {
    python $PyScript
}
