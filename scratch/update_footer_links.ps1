# Update footer legal links across all HTML files in root and tours/
$rootDir  = "c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
$toursDir = Join-Path $rootDir "tours"

$rootFiles = Get-ChildItem -Path $rootDir  -Filter "*.html" -File
$tourFiles = Get-ChildItem -Path $toursDir -Filter "*.html" -File

$updatedCount = 0

foreach ($f in $rootFiles) {
    $content = Get-Content $f.FullName -Raw -Encoding UTF8
    $newContent = $content -replace '<a href="#">Privacy Policy</a>', '<a href="privacy-policy">Privacy Policy</a>'
    $newContent = $newContent -replace '<a href="#">Terms &amp; Conditions</a>', '<a href="terms-conditions">Terms &amp; Conditions</a>'
    $newContent = $newContent -replace '<a href="#">Terms & Conditions</a>', '<a href="terms-conditions">Terms &amp; Conditions</a>'
    
    if ($newContent -ne $content) {
        Set-Content -Path $f.FullName -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "Updated root file: $($f.Name)" -ForegroundColor Green
        $updatedCount++
    }
}

foreach ($f in $tourFiles) {
    $content = Get-Content $f.FullName -Raw -Encoding UTF8
    $newContent = $content -replace '<a href="#">Privacy Policy</a>', '<a href="../privacy-policy">Privacy Policy</a>'
    $newContent = $newContent -replace '<a href="#">Terms &amp; Conditions</a>', '<a href="../terms-conditions">Terms &amp; Conditions</a>'
    $newContent = $newContent -replace '<a href="#">Terms & Conditions</a>', '<a href="../terms-conditions">Terms &amp; Conditions</a>'
    
    if ($newContent -ne $content) {
        Set-Content -Path $f.FullName -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "Updated tour file: $($f.Name)" -ForegroundColor Green
        $updatedCount++
    }
}

Write-Host "Total files updated with footer legal links: $updatedCount" -ForegroundColor Cyan
