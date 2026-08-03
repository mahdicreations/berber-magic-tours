<?php
header('Content-Type: application/json; charset=utf-8');

// DEBUG: Show exactly what PHP receives
echo json_encode([
    'status' => 'debug',
    'POST' => $_POST,
    'REQUEST' => $_REQUEST,
    'raw_input' => file_get_contents('php://input'),
    'content_type' => $_SERVER['CONTENT_TYPE'] ?? 'none',
    'method' => $_SERVER['REQUEST_METHOD']
]);
