$rootDir = "c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

# Check contact.html for any remaining internal .html hrefs
$content = Get-Content (Join-Path $rootDir "contact.html") -Raw

# Find href="...." containing .html (but not external URLs)
$matches2 = [System.Text.RegularExpressions.Regex]::Matches($content, 'href="(?!https?://|mailto:|tel:)([^"]*?\.html)"')
if ($matches2.Count -gt 0) {
    Write-Host "contact.html still has .html links:" -ForegroundColor Red
    foreach ($m in $matches2) { Write-Host "  " $m.Value }
} else {
    Write-Host "contact.html: OK - no internal .html links found" -ForegroundColor Green
}

# Check a tour page
$content2 = Get-Content (Join-Path $rootDir "tours\3days-merzouga-desert.html") -Raw
$matches3 = [System.Text.RegularExpressions.Regex]::Matches($content2, 'href="(?!https?://|mailto:|tel:)([^"]*?\.html)"')
if ($matches3.Count -gt 0) {
    Write-Host "tours/3days-merzouga-desert.html still has .html links:" -ForegroundColor Red
    foreach ($m in $matches3) { Write-Host "  " $m.Value }
} else {
    Write-Host "tours/3days-merzouga-desert.html: OK - no internal .html links found" -ForegroundColor Green
}

# Check canonical present in faq.html
$faqContent = Get-Content (Join-Path $rootDir "faq.html") -Raw
if ($faqContent -match 'rel="canonical"') {
    Write-Host "faq.html: canonical tag present - OK" -ForegroundColor Green
} else {
    Write-Host "faq.html: MISSING canonical!" -ForegroundColor Red
}

# Count YOUR_LINK_HERE occurrences in contact.html
$socialCount = ([System.Text.RegularExpressions.Regex]::Matches($content, 'YOUR_LINK_HERE')).Count
Write-Host "contact.html: $socialCount dead-link placeholders found" -ForegroundColor Cyan
