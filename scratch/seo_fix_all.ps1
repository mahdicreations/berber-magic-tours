# ============================================================
# SEO Fix Script for Berber Magic Tours
# Applies to ALL .html files in root and tours/ subdirectory
# ============================================================

$baseUrl  = "https://berber-magic-tours.com"
$rootDir  = "c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
$toursDir = Join-Path $rootDir "tours"

# Collect all HTML files
$rootFiles  = Get-ChildItem -Path $rootDir  -Filter "*.html" -File
$tourFiles  = Get-ChildItem -Path $toursDir -Filter "*.html" -File

$allFiles = @()
foreach ($f in $rootFiles)  { $allFiles += @{ File = $f; Prefix = "" } }
foreach ($f in $tourFiles)  { $allFiles += @{ File = $f; Prefix = "tours/" } }

$processed = 0
$skipped   = 0

foreach ($entry in $allFiles) {
    $file   = $entry.File
    $prefix = $entry.Prefix

    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # ----------------------------------------------------------------
    # Derive canonical URL from filename
    # ----------------------------------------------------------------
    $slug = $file.BaseName  # filename without extension
    if ($slug -eq "index") {
        $canonicalUrl = "$baseUrl/"
    } else {
        $canonicalUrl = "$baseUrl/$prefix$slug"
    }

    # ----------------------------------------------------------------
    # Skip if canonical already exists (already processed)
    # ----------------------------------------------------------------
    if ($content -match 'rel="canonical"') {
        Write-Host "SKIP (already has canonical): $($file.Name)" -ForegroundColor Yellow
        $skipped++
        continue
    }

    # ----------------------------------------------------------------
    # Extract existing <title> for OG title
    # ----------------------------------------------------------------
    $ogTitle = ""
    if ($content -match '<title>([^<]+)</title>') {
        $ogTitle = $matches[1].Trim()
    }

    # ----------------------------------------------------------------
    # Extract existing meta description for OG description
    # ----------------------------------------------------------------
    $ogDesc = ""
    if ($content -match '<meta\s+name="description"\s+content="([^"]+)"') {
        $ogDesc = $matches[1].Trim()
    }

    # ----------------------------------------------------------------
    # Build the canonical + OG block to insert after <meta name="description">
    # ----------------------------------------------------------------
    $ogBlock = @"
    <link rel="canonical" href="$canonicalUrl" />
    <meta property="og:title" content="$ogTitle">
    <meta property="og:description" content="$ogDesc">
    <meta property="og:image" content="https://berber-magic-tours.com/assets/images/logo.png">
    <meta property="og:url" content="$canonicalUrl">
    <meta property="og:type" content="website">
"@

    # Insert after the meta description line
    $content = $content -replace '(<meta\s+name="description"[^>]+>)', "`$1`r`n$ogBlock"

    # ----------------------------------------------------------------
    # Fix 1: Remove .html from ALL internal hrefs
    #   - Match href="something.html" where something does NOT start with http/https/mailto/tel/#
    #   - Handle both relative and root-relative hrefs
    # ----------------------------------------------------------------

    # href="index.html" → href="/"
    $content = $content -replace 'href="index\.html"', 'href="/"'

    # href="page.html" (root-level pages from root files, no path prefix)
    # href="../page.html" (from tours/ subdirectory, going up one level)
    # href="tours/page.html"

    # General pattern: remove .html from internal (non-http/mailto/tel) links
    # We use a regex that matches href="..." where the value doesn't start with http, mailto, tel, #
    $content = [System.Text.RegularExpressions.Regex]::Replace(
        $content,
        'href="(?!https?://|mailto:|tel:|#|/)([^"]*?)\.html"',
        'href="$1"'
    )

    # ----------------------------------------------------------------
    # Fix 2: Replace href="#" on social media / dead links
    #   Only target <a> elements that have social/tripadvisor icons inside them
    #   OR are in top-bar-socials / social-links / btn-tripadvisor context
    #   Simple approach: replace any href="#" that is adjacent to social/TripAdvisor classes
    # ----------------------------------------------------------------

    # Top bar socials (fa-facebook-f, fa-instagram, fa-tripadvisor on same line as href="#")
    $content = [System.Text.RegularExpressions.Regex]::Replace(
        $content,
        '(<a\s+)href="#"(\s+target="_blank"><i class="fab fa-(facebook-f|instagram|tripadvisor|linkedin-in)")',
        '$1href="YOUR_LINK_HERE"$2'
    )

    # Social links with title attribute (footer social bar)
    $content = [System.Text.RegularExpressions.Regex]::Replace(
        $content,
        '(<a\s+)href="#"(\s+target="_blank"\s+title="(?:Facebook|Instagram|LinkedIn|TripAdvisor)")',
        '$1href="YOUR_LINK_HERE"$2'
    )

    # btn-tripadvisor "View Reviews" button
    $content = $content -replace 'href="#" class="btn btn-tripadvisor"', 'href="YOUR_LINK_HERE" class="btn btn-tripadvisor"'

    # ----------------------------------------------------------------
    # Write back
    # ----------------------------------------------------------------
    Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
    Write-Host "DONE: $prefix$($file.Name)" -ForegroundColor Green
    $processed++
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Processed : $processed files" -ForegroundColor Green
Write-Host "Skipped   : $skipped files (already had canonical)" -ForegroundColor Yellow
Write-Host "============================================" -ForegroundColor Cyan
