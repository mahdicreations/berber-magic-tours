<?php
header('Content-Type: application/json; charset=utf-8');

// Enable error display for debugging (remove in production)
ini_set('display_errors', 0);
error_reporting(E_ALL);

// SMTP Configuration
$smtp_user = 'info@berber-magic-tours.com';
$smtp_pass = '@berber-magic-tours2026';
$to_email  = 'berbermagictours@gmail.com';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
    exit;
}

// Log raw input for debugging
$raw_input = file_get_contents('php://input');
$content_type = isset($_SERVER['CONTENT_TYPE']) ? $_SERVER['CONTENT_TYPE'] : '';

// Extract parameters - try $_POST first, then JSON body
$params = [];

if (!empty($_POST)) {
    $params = $_POST;
} elseif (!empty($raw_input)) {
    // Try JSON
    $json = json_decode($raw_input, true);
    if (is_array($json)) {
        $params = $json;
    } else {
        // Try URL-encoded
        parse_str($raw_input, $params);
    }
}

// Also check $_REQUEST as fallback
if (empty($params) && !empty($_REQUEST)) {
    $params = $_REQUEST;
}

// --- Parameter extraction ---
$tour_name  = '';
$form_type  = 'Tour Booking Request';
$name       = '';
$email      = '';
$phone      = 'N/A';
$date       = 'Not specified';
$travelers  = '2';
$style      = 'Standard';
$message    = '';

foreach ($params as $key => $val) {
    $k = strtolower(trim($key));
    $v = is_string($val) ? trim($val) : strval($val);
    if ($v === '' || $v === null) continue;

    if (in_array($k, ['tour_name', 'tourname', 'tour'])) {
        $tour_name = $v;
    } elseif (in_array($k, ['form_type', 'formtype'])) {
        $form_type = $v;
    } elseif (in_array($k, ['name', 'full_name', 'fullname', 'customer_name'])) {
        $name = $v;
    } elseif (in_array($k, ['email', 'email_address', 'user_email', 'customer_email'])) {
        $email = $v;
    } elseif (in_array($k, ['phone', 'tel', 'whatsapp'])) {
        $phone = $v;
    } elseif (in_array($k, ['date', 'travel_date'])) {
        $date = $v;
    } elseif (in_array($k, ['travelers', 'people', 'guests'])) {
        $travelers = $v;
    } elseif (in_array($k, ['travel_style', 'style', 'travelstyle'])) {
        $style = $v;
    } elseif (in_array($k, ['message', 'requests', 'notes'])) {
        $message = $v;
    }
}

// Default tour name fallback
if (empty($tour_name)) $tour_name = 'Morocco Tour';

// Build subject
$subject_name = !empty($name) ? $name : 'New Visitor';
$subject = "Tour Booking: " . $tour_name . " — " . $subject_name;

// Build HTML Body
$display_name  = !empty($name)  ? htmlspecialchars($name)      : '<span style="color:#e74c3c">Not provided</span>';
$display_email = !empty($email) ? htmlspecialchars($email)      : '<span style="color:#e74c3c">Not provided</span>';
$display_phone = !empty($phone) ? htmlspecialchars($phone)      : 'N/A';
$display_date  = !empty($date)  ? htmlspecialchars($date)       : 'Not specified';
$display_count = !empty($travelers) ? htmlspecialchars($travelers) : '2';
$display_style = !empty($style) ? htmlspecialchars($style)      : 'Standard';
$display_msg   = !empty($message) ? nl2br(htmlspecialchars($message)) : '';

// Debug row showing all raw received params
$raw_params_debug = '';
if (!empty($params)) {
    foreach ($params as $k => $v) {
        $raw_params_debug .= '<tr style="font-size:11px;"><td style="color:#94A3B8;padding:2px 6px;">' 
            . htmlspecialchars($k) . '</td><td style="color:#64748B;padding:2px 6px;">' 
            . htmlspecialchars(strval($v)) . '</td></tr>';
    }
}

$body_html = '<!DOCTYPE html><html><head><meta charset="utf-8"></head>'
    . '<body style="margin:0;padding:0;background:#F4F6F8;font-family:\'Segoe UI\',Tahoma,sans-serif;">'
    . '<table width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#F4F6F8;padding:30px 10px;"><tr><td align="center">'
    . '<table width="600" cellpadding="0" cellspacing="0" border="0" style="background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.08);">'
    
    // Header
    . '<tr><td style="background:linear-gradient(135deg,#1E293B,#0F172A);padding:28px 30px;text-align:center;">'
    . '<h1 style="color:#fff;margin:0;font-size:22px;font-weight:700;letter-spacing:1px;">BERBER MAGIC TOURS</h1>'
    . '<p style="color:#D95D39;margin:6px 0 0 0;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;">New Tour Booking Request</p>'
    . '</td></tr>'
    
    // Body
    . '<tr><td style="padding:28px 30px;">'
    . '<h2 style="color:#1E293B;font-size:17px;margin:0 0 15px;border-bottom:2px solid #F1F5F9;padding-bottom:10px;">' . htmlspecialchars($tour_name) . '</h2>'
    . '<table width="100%" cellpadding="8" cellspacing="0" border="0" style="border-collapse:collapse;">'
    
    . '<tr style="border-bottom:1px solid #F1F5F9;"><td width="38%" style="font-weight:600;color:#1E293B;font-size:14px;">Selected Tour:</td><td style="color:#475569;font-size:14px;"><strong>' . htmlspecialchars($tour_name) . '</strong></td></tr>'
    . '<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600;color:#1E293B;font-size:14px;">Full Name:</td><td style="color:#475569;font-size:14px;">' . $display_name . '</td></tr>'
    . '<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600;color:#1E293B;font-size:14px;">Email Address:</td><td style="color:#475569;font-size:14px;">' . $display_email . '</td></tr>'
    . '<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600;color:#1E293B;font-size:14px;">WhatsApp / Phone:</td><td style="color:#475569;font-size:14px;">' . $display_phone . '</td></tr>'
    . '<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600;color:#1E293B;font-size:14px;">Travel Date:</td><td style="color:#475569;font-size:14px;">' . $display_date . '</td></tr>'
    . '<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600;color:#1E293B;font-size:14px;">Travelers:</td><td style="color:#475569;font-size:14px;">' . $display_count . ' person(s)</td></tr>'
    . '<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600;color:#1E293B;font-size:14px;">Travel Style:</td><td style="color:#D95D39;font-weight:700;font-size:14px;">' . $display_style . '</td></tr>'
    . (!empty($display_msg) ? '<tr style="border-bottom:1px solid #F1F5F9;"><td style="font-weight:600;color:#1E293B;font-size:14px;">Special Requests:</td><td style="color:#475569;font-size:14px;">' . $display_msg . '</td></tr>' : '')
    
    . '</table>'
    
    // Contact box
    . '<div style="background:#FFF7F2;border-left:4px solid #D95D39;padding:14px 18px;border-radius:6px;margin-top:20px;">'
    . '<p style="margin:0;color:#D95D39;font-weight:700;font-size:14px;">Customer Contact:</p>'
    . '<p style="margin:6px 0 0;color:#475569;font-size:14px;">Email: <a href="mailto:' . htmlspecialchars($email) . '" style="color:#D95D39;font-weight:600;">' . $display_email . '</a><br>'
    . 'Phone / WhatsApp: <strong>' . $display_phone . '</strong></p>'
    . '</div>'
    
    . '</td></tr>'
    
    // Footer
    . '<tr><td style="background:#F8FAFC;padding:16px 30px;text-align:center;border-top:1px solid #E2E8F0;color:#94A3B8;font-size:11px;">Sent automatically from Berber Magic Tours website booking system.</td></tr>'
    
    . '</table></td></tr></table></body></html>';

// --- SMTP Socket Mailer ---
function send_smtp($host, $port, $username, $password, $from, $to, $subject, $html_content, $reply_to = '') {
    $context = stream_context_create([
        'ssl' => [
            'verify_peer' => false,
            'verify_peer_name' => false,
            'allow_self_signed' => true
        ]
    ]);
    $prefix = ($port == 465) ? 'ssl://' : '';
    $socket = @stream_socket_client("{$prefix}{$host}:{$port}", $errno, $errstr, 15, STREAM_CLIENT_CONNECT, $context);
    if (!$socket) return false;
    
    fgets($socket, 512);
    fputs($socket, "EHLO localhost\r\n");
    while ($line = fgets($socket, 512)) {
        if (substr($line, 3, 1) == ' ') break;
    }
    
    fputs($socket, "AUTH LOGIN\r\n");
    fgets($socket, 512);
    fputs($socket, base64_encode($username) . "\r\n");
    fgets($socket, 512);
    fputs($socket, base64_encode($password) . "\r\n");
    $auth_response = fgets($socket, 512);
    if (substr($auth_response, 0, 3) != '235') {
        fclose($socket);
        return false;
    }
    
    fputs($socket, "MAIL FROM: <{$from}>\r\n");
    fgets($socket, 512);
    fputs($socket, "RCPT TO: <{$to}>\r\n");
    fgets($socket, 512);
    fputs($socket, "DATA\r\n");
    fgets($socket, 512);
    
    $reply_header = !empty($reply_to) ? "Reply-To: {$reply_to}\r\n" : "Reply-To: {$from}\r\n";
    $headers  = "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $headers .= "From: Berber Magic Tours <{$from}>\r\n";
    $headers .= "Sender: {$from}\r\n";
    $headers .= "Return-Path: <{$from}>\r\n";
    $headers .= $reply_header;
    $headers .= "To: {$to}\r\n";
    $headers .= "Subject: {$subject}\r\n";
    
    fputs($socket, $headers . "\r\n" . $html_content . "\r\n.\r\n");
    fgets($socket, 512);
    fputs($socket, "QUIT\r\n");
    fclose($socket);
    return true;
}

// Try SMTP hosts
$hosts = [
    ['host' => 'localhost',                         'port' => 25],
    ['host' => '127.0.0.1',                        'port' => 25],
    ['host' => 'localhost',                         'port' => 465],
    ['host' => 'berber-magic-tours.com',           'port' => 465],
    ['host' => 'mail.berber-magic-tours.com',      'port' => 465],
    ['host' => 'premium705.web-hosting.com',        'port' => 465],
];

$sent = false;
$reply_to_email = !empty($email) ? $email : $smtp_user;

foreach ($hosts as $h) {
    if (send_smtp($h['host'], $h['port'], $smtp_user, $smtp_pass, $smtp_user, $to_email, $subject, $body_html, $reply_to_email)) {
        $sent = true;
        break;
    }
}

if (!$sent) {
    // Fallback: native PHP mail()
    $mail_headers  = "MIME-Version: 1.0\r\n";
    $mail_headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $mail_headers .= "From: Berber Magic Tours <{$smtp_user}>\r\n";
    $mail_headers .= "Sender: {$smtp_user}\r\n";
    $mail_headers .= "Return-Path: <{$smtp_user}>\r\n";
    $mail_headers .= "Reply-To: {$reply_to_email}\r\n";
    @mail($to_email, $subject, $body_html, $mail_headers, "-f {$smtp_user}");
}

$tour_display = !empty($tour_name) ? $tour_name : 'your selected tour';

echo json_encode([
    'status'  => 'success',
    'message' => 'Thank you! Your reservation request for ' . htmlspecialchars($tour_display) . ' has been submitted. Our team will contact you within 24 hours.'
]);
