# Add footer signature to all HTML files
$rootDir  = "c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
$toursDir = Join-Path $rootDir "tours"

$rootFiles = Get-ChildItem -Path $rootDir  -Filter "*.html" -File
$tourFiles = Get-ChildItem -Path $toursDir -Filter "*.html" -File

$allFiles = $rootFiles + $tourFiles

$sig = @"
            <div class="footer-signature">
                Designed with <i class="fas fa-heart"></i> by <a href="https://mahdicreations.dev" target="_blank" rel="noopener">mahdicreations.dev</a>
            </div>
"@

$updated = 0

foreach ($f in $allFiles) {
    $content = Get-Content $f.FullName -Raw -Encoding UTF8

    # Skip if signature already added
    if ($content -match 'mahdicreations\.dev') {
        continue
    }

    # Match <div class="footer-bottom">...</div>
    # and insert signature right after it
    if ($content -match '(?s)(<div class="footer-bottom">.*?</div>)') {
        $matchedBlock = $matches[1]
        $replacement = "$matchedBlock`r`n$sig"
        
        # Replace only the first match of footer-bottom
        $index = $content.IndexOf($matchedBlock)
        if ($index -ge 0) {
            $newContent = $content.Substring(0, $index) + $replacement + $content.Substring($index + $matchedBlock.Length)
            Set-Content -Path $f.FullName -Value $newContent -Encoding UTF8 -NoNewline
            $updated++
            Write-Host "Added signature to $($f.Name)" -ForegroundColor Green
        }
    } else {
        Write-Host "WARNING: No footer-bottom found in $($f.Name)" -ForegroundColor Yellow
    }
}

Write-Host "Total files updated: $updated" -ForegroundColor Cyan
