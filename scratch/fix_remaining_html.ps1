# Full fix: remove .html from ALL remaining internal hrefs across every page
$rootDir  = "c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
$pattern  = 'href="(?!https?://|mailto:|tel:)([^"]*?)\.html"'

$rootFiles = Get-ChildItem -Path $rootDir  -Filter "*.html" -File
$tourFiles = Get-ChildItem -Path (Join-Path $rootDir "tours") -Filter "*.html" -File

$allFiles = @()
foreach ($f in $rootFiles) { $allFiles += @{ File = $f; Label = $f.Name } }
foreach ($f in $tourFiles) { $allFiles += @{ File = $f; Label = "tours/$($f.Name)" } }

$fixedFiles = 0
$totalFixed = 0

foreach ($entry in $allFiles) {
    $file    = $entry.File
    $label   = $entry.Label
    $content = Get-Content $file.FullName -Raw

    $before = ([System.Text.RegularExpressions.Regex]::Matches($content, $pattern)).Count

    if ($before -gt 0) {
        # Remove .html from all internal hrefs (non-http, non-mailto, non-tel)
        $content = [System.Text.RegularExpressions.Regex]::Replace(
            $content,
            $pattern,
            'href="$1"'
        )

        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline

        $after = ([System.Text.RegularExpressions.Regex]::Matches($content, $pattern)).Count
        Write-Host "FIXED [$label]: $before links cleaned ($after remaining)" -ForegroundColor Green
        $fixedFiles++
        $totalFixed += $before
    }
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Files updated : $fixedFiles" -ForegroundColor Green
Write-Host "Links cleaned : $totalFixed" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
