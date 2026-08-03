<?php
header('Content-Type: application/json; charset=utf-8');

// Enable error reporting for debugging if needed
error_reporting(0);

// Configuration
$smtp_host = 'berber-magic-tours.com';
$smtp_port = 465; // SSL
$smtp_user = 'info@berber-magic-tours.com';
$smtp_pass = '@berber-magic-tours2026';
$to_email  = 'javarx@gmail.com';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['status' => 'error', 'message' => 'Invalid request method.']);
    exit;
}

// Retrieve POST parameters
$form_type   = isset($_POST['form_type']) ? trim($_POST['form_type']) : 'Tour Booking Request';
$tour_name   = isset($_POST['tour_name']) ? trim($_POST['tour_name']) : '';
$name        = isset($_POST['name']) ? trim($_POST['name']) : '';
$email       = isset($_POST['email']) ? trim($_POST['email']) : '';
$phone       = isset($_POST['phone']) ? trim($_POST['phone']) : 'N/A';
$date        = isset($_POST['date']) ? trim($_POST['date']) : '';
$travelers   = isset($_POST['travelers']) ? trim($_POST['travelers']) : '';
$style       = isset($_POST['travel_style']) ? trim($_POST['travel_style']) : '';
$duration    = isset($_POST['duration']) ? trim($_POST['duration']) : '';
$includes    = isset($_POST['includes']) ? trim($_POST['includes']) : '';
$message     = isset($_POST['message']) ? trim($_POST['message']) : '';

if (empty($name) || empty($email)) {
    echo json_encode(['status' => 'error', 'message' => 'Please provide both your Name and Email address.']);
    exit;
}

$subject = "New " . ($tour_name ? "Booking: " . $tour_name : "Inquiry") . " - " . $name;

// Build HTML Rows
$rows_html = '';
function addRow(&$html, $label, $value) {
    if (!empty($value)) {
        $html .= '<tr style="border-bottom:1px solid #F1F5F9;">'
               . '<td width="38%" style="font-weight:600; color:#1E293B; padding:10px 0; font-size:14px;">' . htmlspecialchars($label) . ':</td>'
               . '<td style="color:#475569; padding:10px 0; font-size:14px;">' . nl2br(htmlspecialchars($value)) . '</td>'
               . '</tr>';
    }
}

if (!empty($tour_name)) addRow($rows_html, 'Selected Tour', $tour_name);
addRow($rows_html, 'Full Name', $name);
addRow($rows_html, 'Email Address', $email);
addRow($rows_html, 'WhatsApp / Phone', $phone);
if (!empty($date)) addRow($rows_html, 'Travel Date', $date);
if (!empty($travelers)) addRow($rows_html, 'Travelers Count', $travelers);
if (!empty($style)) addRow($rows_html, 'Travel Style', $style);
if (!empty($duration)) addRow($rows_html, 'Trip Duration', $duration);
if (!empty($includes)) addRow($rows_html, 'Included Activities', $includes);
if (!empty($message)) addRow($rows_html, 'Special Requests / Message', $message);

// Build Email Template
$body_html = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body style="margin:0; padding:0; background-color:#F4F6F8; font-family:\'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif; color:#333;">'
           . '<table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#F4F6F8; padding: 40px 10px;"><tr><td align="center">'
           . '<table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color:#ffffff; border-radius:16px; overflow:hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">'
           . '<tr><td style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 32px 30px; text-align: center;">'
           . '<h1 style="color:#ffffff; margin:0; font-size:22px; font-weight:700; letter-spacing:1px;">BERBER MAGIC TOURS</h1>'
           . '<p style="color:#D95D39; margin:6px 0 0 0; font-size:13px; font-weight:600; text-transform:uppercase; letter-spacing:1.5px;">New Website Reservation</p>'
           . '</td></tr>'
           . '<tr><td style="padding: 30px;">'
           . '<h2 style="color:#1E293B; font-size:18px; margin-top:0; margin-bottom:15px; border-bottom:2px solid #F1F5F9; padding-bottom:10px;">' . htmlspecialchars($form_type) . '</h2>'
           . '<table border="0" cellpadding="8" cellspacing="0" width="100%" style="border-collapse:collapse; margin-bottom:20px;">' . $rows_html . '</table>'
           . '<div style="background-color:#FFF7F2; border-left:4px solid #D95D39; padding:15px 20px; border-radius:6px; margin-top:20px;">'
           . '<p style="margin:0; color:#D95D39; font-weight:700; font-size:14px;">Customer Direct Contact:</p>'
           . '<p style="margin:5px 0 0 0; color:#475569; font-size:14px;">Email: <a href="mailto:' . htmlspecialchars($email) . '" style="color:#D95D39; text-decoration:none; font-weight:600;">' . htmlspecialchars($email) . '</a><br>Phone / WhatsApp: <strong>' . htmlspecialchars($phone) . '</strong></p>'
           . '</div>'
           . '</td></tr>'
           . '<tr><td style="background-color:#F8FAFC; padding:20px 30px; text-align:center; border-top:1px solid #E2E8F0; color:#94A3B8; font-size:12px;">Sent automatically from Berber Magic Tours website booking system.</td></tr>'
           . '</table></td></tr></table></body></html>';

// Send via SMTP SSL Port 465
function send_smtp_email($host, $port, $username, $password, $from, $to, $subject, $html_content, $reply_to) {
    $context = stream_context_create([
        'ssl' => [
            'verify_peer' => false,
            'verify_peer_name' => false,
            'allow_self_signed' => true
        ]
    ]);
    
    $socket = @stream_socket_client("ssl://{$host}:{$port}", $errno, $errstr, 20, STREAM_CLIENT_CONNECT, $context);
    if (!$socket) {
        return false;
    }
    
    fgets($socket, 512);
    
    fputs($socket, "EHLO {$host}\r\n");
    while ($line = fgets($socket, 512)) {
        if (substr($line, 3, 1) == ' ') break;
    }
    
    fputs($socket, "AUTH LOGIN\r\n");
    fgets($socket, 512);
    
    fputs($socket, base64_encode($username) . "\r\n");
    fgets($socket, 512);
    
    fputs($socket, base64_encode($password) . "\r\n");
    $auth_res = fgets($socket, 512);
    if (substr($auth_res, 0, 3) != '235') {
        fclose($socket);
        return false;
    }
    
    fputs($socket, "MAIL FROM: <{$from}>\r\n");
    fgets($socket, 512);
    
    fputs($socket, "RCPT TO: <{$to}>\r\n");
    fgets($socket, 512);
    
    fputs($socket, "DATA\r\n");
    fgets($socket, 512);
    
    $headers  = "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $headers .= "From: Berber Magic Tours <{$from}>\r\n";
    $headers .= "Reply-To: {$reply_to}\r\n";
    $headers .= "To: {$to}\r\n";
    $headers .= "Subject: {$subject}\r\n";
    
    fputs($socket, $headers . "\r\n" . $html_content . "\r\n.\r\n");
    fgets($socket, 512);
    
    fputs($socket, "QUIT\r\n");
    fclose($socket);
    
    return true;
}

$sent = send_smtp_email($smtp_host, $smtp_port, $smtp_user, $smtp_pass, $smtp_user, $to_email, $subject, $body_html, $email);

if ($sent) {
    echo json_encode(['status' => 'success', 'message' => 'Thank you! Your reservation request has been submitted successfully. Our team will get back to you shortly.']);
} else {
    // Fallback to mail()
    $headers  = "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $headers .= "From: Berber Magic Tours <{$smtp_user}>\r\n";
    $headers .= "Reply-To: {$email}\r\n";
    
    if (@mail($to_email, $subject, $body_html, $headers)) {
        echo json_encode(['status' => 'success', 'message' => 'Thank you! Your request has been submitted successfully.']);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'Submission failed. Please contact us directly via WhatsApp or Email.']);
    }
}
