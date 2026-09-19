<?php
// router.php - Development server router for Berber Magic Tours
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$uri = urldecode($uri);

$docRoot = realpath(__DIR__);
$targetPath = realpath($docRoot . $uri);

// Prevent path traversal outside root
if ($targetPath !== false && strpos($targetPath, $docRoot) !== 0) {
    http_response_code(403);
    echo "403 Forbidden";
    return true;
}

// 1. Existing file check
if ($targetPath !== false && is_file($targetPath)) {
    // If it's a PHP file, execute it
    if (pathinfo($targetPath, PATHINFO_EXTENSION) === 'php') {
        require $targetPath;
        return true;
    }
    // Static file: let PHP built-in server handle MIME type and streaming
    return false;
}

// 2. Directory check (e.g. / or /blog/)
if ($targetPath !== false && is_dir($targetPath)) {
    $indexHtml = $targetPath . DIRECTORY_SEPARATOR . 'index.html';
    $indexPhp  = $targetPath . DIRECTORY_SEPARATOR . 'index.php';
    if (is_file($indexHtml)) {
        header('Content-Type: text/html; charset=UTF-8');
        readfile($indexHtml);
        return true;
    }
    if (is_file($indexPhp)) {
        require $indexPhp;
        return true;
    }
}

// 3. Clean URLs (e.g. /about-us -> /about-us.html or /tours/2-days-mount-toubkal -> /tours/2-days-mount-toubkal.html)
$candidateHtml = $docRoot . rtrim($uri, '/') . '.html';
if (is_file($candidateHtml)) {
    header('Content-Type: text/html; charset=UTF-8');
    readfile($candidateHtml);
    return true;
}

// 4. Fallback 404
http_response_code(404);
$notFoundPage = $docRoot . DIRECTORY_SEPARATOR . '404.html';
if (is_file($notFoundPage)) {
    header('Content-Type: text/html; charset=UTF-8');
    readfile($notFoundPage);
    return true;
}

echo "404 Not Found";
return true;
