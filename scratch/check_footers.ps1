# Check footer-bottom variations
$rootDir  = "c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
$toursDir = Join-Path $rootDir "tours"

$rootFiles = Get-ChildItem -Path $rootDir  -Filter "*.html" -File
$tourFiles = Get-ChildItem -Path $toursDir -Filter "*.html" -File

$allFiles = $rootFiles + $tourFiles

foreach ($f in $allFiles) {
    $content = Get-Content $f.FullName -Raw
    if ($content -notmatch 'class="footer-bottom"') {
        Write-Host "No footer-bottom in: $($f.Name)" -ForegroundColor Red
    }
}
Write-Host "Check complete." -ForegroundColor Green
