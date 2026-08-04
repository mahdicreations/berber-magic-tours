# Scan ALL html files for any remaining internal .html hrefs
$rootDir  = "c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
$pattern  = 'href="(?!https?://|mailto:|tel:)([^"]*?\.html)"'

$rootFiles = Get-ChildItem -Path $rootDir  -Filter "*.html" -File
$tourFiles = Get-ChildItem -Path (Join-Path $rootDir "tours") -Filter "*.html" -File

$allFiles = @()
foreach ($f in $rootFiles) { $allFiles += @{ File = $f; Label = $f.Name } }
foreach ($f in $tourFiles) { $allFiles += @{ File = $f; Label = "tours/$($f.Name)" } }

$totalHits = 0

foreach ($entry in $allFiles) {
    $file    = $entry.File
    $label   = $entry.Label
    $content = Get-Content $file.FullName -Raw

    $matches2 = [System.Text.RegularExpressions.Regex]::Matches($content, $pattern)
    if ($matches2.Count -gt 0) {
        Write-Host "`n[$label] - $($matches2.Count) remaining .html link(s):" -ForegroundColor Red
        foreach ($m in $matches2) {
            Write-Host "   $($m.Value)" -ForegroundColor Yellow
        }
        $totalHits += $matches2.Count
    }
}

if ($totalHits -eq 0) {
    Write-Host "`nAll clean! No internal .html links found." -ForegroundColor Green
} else {
    Write-Host "`nTotal remaining: $totalHits links still have .html" -ForegroundColor Red
}
