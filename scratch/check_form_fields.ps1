Select-String -Path "tours\2-days-mount-toubkal.html" -Pattern "widget-title|widget-subtitle|tour_name|book-name|book-email|book-phone|book-date|book-travelers|travel-style|book-message" | ForEach-Object {
    Write-Host ($_.LineNumber.ToString() + ": " + $_.Line.Trim())
}
