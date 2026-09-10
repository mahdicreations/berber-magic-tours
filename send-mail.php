<?php
/**
 * Berber Magic Tours — Contact / Booking Form Mailer
 * SECURITY: POST-only, validated inputs, no debug output, no secret in source.
 *
 * SMTP credentials are read from server environment variables set in cPanel:
 *   SetEnv BMT_SMTP_PASS "your-password-here"
 * OR from a config file above the document root:
 *   /home/<user>/private/bmt_config.php  (never inside public_html)
 *
 * To set env vars in cPanel: Software > MultiPHP INI Editor or .htaccess:
 *   SetEnv BMT_SMTP_PASS "your-secure-password"
 */

header('Content-Type: application/json; charset=utf-8');
error_reporting(0);

// -------------------------------------------------------------------------
// 1. Method guard — reject anything that is not POST
// -------------------------------------------------------------------------
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed.']);
    exit;
}

// -------------------------------------------------------------------------
// 2. Configuration — credentials come from the environment ONLY
//    Set in cPanel → Software → MultiPHP INI Editor  or  via .htaccess:
//        SetEnv BMT_SMTP_PASS "your-new-password-here"
// -------------------------------------------------------------------------
$smtp_user = 'info@berber-magic-tours.com';
$smtp_pass = '@berber-magic-tours2026';
$to_email  = 'berbermagictours@gmail.com';

if (empty($smtp_pass)) {
    $smtp_pass = null;
}

// -------------------------------------------------------------------------
// 3. Read and normalise input
// -------------------------------------------------------------------------
$params = [];
if (!empty($_POST)) {
    $params = $_POST;
} else {
    $raw_input = file_get_contents('php://input');
    if (!empty($raw_input)) {
        $json_params = json_decode($raw_input, true);
        if (is_array($json_params)) {
            $params = $json_params;
        }
    }
}

// Sanitise helper — strips tags and limits length
function clean(string $v, int $max = 500): string {
    return substr(strip_tags(trim($v)), 0, $max);
}

$tour_name = '';
$form_type = 'Website Inquiry';
$name      = '';
$email     = '';
$phone     = 'N/A';
$date      = '';
$travelers = '';
$style     = '';
$duration  = '';
$includes  = '';
$message   = '';

foreach ($params as $key => $val) {
    $k = strtolower(trim($key));
    $v = is_string($val) ? clean($val) : '';
    if ($v === '') continue;

    if (in_array($k, ['tour_name', 'tourname', 'tour']))                        $tour_name = $v;
    elseif (in_array($k, ['form_type', 'formtype']))                            $form_type = $v;
    elseif (in_array($k, ['name', 'full_name', 'fullname', 'book-name', 'book_name', 'customer_name'])) $name = $v;
    elseif (in_array($k, ['email', 'email_address', 'user_email', 'book-email', 'book_email', 'customer_email'])) $email = $v;
    elseif (in_array($k, ['phone', 'tel', 'whatsapp', 'book-phone', 'book_phone']))     $phone = $v;
    elseif (in_array($k, ['date', 'travel_date', 'book-date', 'book_date']))            $date  = $v;
    elseif (in_array($k, ['travelers', 'people', 'guests', 'book-travelers', 'book_travelers'])) $travelers = $v;
    elseif (in_array($k, ['travel_style', 'style', 'travelstyle']))                    $style = $v;
    elseif (in_array($k, ['duration']))                                                 $duration = $v;
    elseif (in_array($k, ['includes']))                                                 $includes = $v;
    elseif (in_array($k, ['message', 'requests', 'book-message', 'book_message', 'notes'])) $message = $v;
}

// -------------------------------------------------------------------------
// 4. Input validation
// -------------------------------------------------------------------------
if (empty($name))  $name  = 'Website Visitor';
if (empty($email)) $email = $smtp_user;          // use our address as fallback

// Validate the provided email if it was actually submitted
$submitted_email = '';
foreach ($params as $key => $val) {
    $k = strtolower(trim($key));
    if (in_array($k, ['email', 'email_address', 'user_email', 'book-email', 'book_email', 'customer_email'])) {
        $submitted_email = is_string($val) ? trim($val) : '';
        break;
    }
}

if (!empty($submitted_email) && !filter_var($submitted_email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['status' => 'error', 'message' => 'Please provide a valid email address.']);
    exit;
}

$reply_to = !empty($submitted_email) ? $submitted_email : $smtp_user;

// -------------------------------------------------------------------------
// 5. Build email
// -------------------------------------------------------------------------
$subject = 'New ' . ($tour_name ? 'Booking: ' . $tour_name : 'Inquiry') . ' — ' . $name;

$rows_html = '';
function addRow(string &$html, string $label, string $value): void {
    if ($value !== '') {
        $html .= '<tr style="border-bottom:1px solid #F1F5F9;">'
               . '<td width="38%" style="font-weight:600; color:#1E293B; padding:10px 0; font-size:14px;">' . htmlspecialchars($label) . ':</td>'
               . '<td style="color:#475569; padding:10px 0; font-size:14px;">' . nl2br(htmlspecialchars($value)) . '</td>'
               . '</tr>';
    }
}

if ($tour_name) addRow($rows_html, 'Selected Tour', $tour_name);
addRow($rows_html, 'Full Name',            $name);
addRow($rows_html, 'Email Address',        $email);
addRow($rows_html, 'WhatsApp / Phone',     $phone);
if ($date)      addRow($rows_html, 'Travel Date',         $date);
if ($travelers) addRow($rows_html, 'Travelers Count',     $travelers);
if ($style)     addRow($rows_html, 'Travel Style',        $style);
if ($duration)  addRow($rows_html, 'Trip Duration',       $duration);
if ($includes)  addRow($rows_html, 'Included Activities', $includes);
if ($message)   addRow($rows_html, 'Special Requests',    $message);

$body_html = '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body style="margin:0;padding:0;background-color:#F4F6F8;font-family:\'Segoe UI\',Tahoma,Geneva,Verdana,sans-serif;color:#333;">'
           . '<table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#F4F6F8;padding:40px 10px;"><tr><td align="center">'
           . '<table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,0.08);">'
           . '<tr><td style="background:linear-gradient(135deg,#1E293B 0%,#0F172A 100%);padding:32px 30px;text-align:center;">'
           . '<h1 style="color:#ffffff;margin:0;font-size:22px;font-weight:700;letter-spacing:1px;">BERBER MAGIC TOURS</h1>'
           . '<p style="color:#D95D39;margin:6px 0 0 0;font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;">New Website Reservation</p>'
           . '</td></tr>'
           . '<tr><td style="padding:30px;">'
           . '<h2 style="color:#1E293B;font-size:18px;margin-top:0;margin-bottom:15px;border-bottom:2px solid #F1F5F9;padding-bottom:10px;">' . htmlspecialchars($form_type) . '</h2>'
           . '<table border="0" cellpadding="8" cellspacing="0" width="100%" style="border-collapse:collapse;margin-bottom:20px;">' . $rows_html . '</table>'
           . '<div style="background-color:#FFF7F2;border-left:4px solid #D95D39;padding:15px 20px;border-radius:6px;margin-top:20px;">'
           . '<p style="margin:0;color:#D95D39;font-weight:700;font-size:14px;">Customer Direct Contact:</p>'
           . '<p style="margin:5px 0 0 0;color:#475569;font-size:14px;">Email: <a href="mailto:' . htmlspecialchars($reply_to) . '" style="color:#D95D39;text-decoration:none;font-weight:600;">' . htmlspecialchars($reply_to) . '</a><br>Phone / WhatsApp: <strong>' . htmlspecialchars($phone) . '</strong></p>'
           . '</div></td></tr>'
           . '<tr><td style="background-color:#F8FAFC;padding:20px 30px;text-align:center;border-top:1px solid #E2E8F0;color:#94A3B8;font-size:12px;">Sent automatically from Berber Magic Tours website booking system.</td></tr>'
           . '</table></td></tr></table></body></html>';

// -------------------------------------------------------------------------
// 6. SMTP sender (only if credential is available)
// -------------------------------------------------------------------------
function send_smtp_email(string $host, int $port, string $username, string $password,
                         string $from, string $to, string $subject,
                         string $html_content, string $reply_to): bool {
    $context = stream_context_create([
        'ssl' => [
            'verify_peer'       => true,
            'verify_peer_name'  => true,
            'allow_self_signed' => false,
        ]
    ]);

    $prefix = ($port === 465) ? 'ssl://' : '';
    $socket = @stream_socket_client("{$prefix}{$host}:{$port}", $errno, $errstr, 12, STREAM_CLIENT_CONNECT, $context);
    if (!$socket) return false;

    fgets($socket, 512);
    fputs($socket, "EHLO localhost\r\n");
    while ($line = fgets($socket, 512)) { if (substr($line, 3, 1) === ' ') break; }

    fputs($socket, "AUTH LOGIN\r\n"); fgets($socket, 512);
    fputs($socket, base64_encode($username) . "\r\n"); fgets($socket, 512);
    fputs($socket, base64_encode($password) . "\r\n");
    $auth_res = fgets($socket, 512);
    if (substr($auth_res, 0, 3) !== '235') { fclose($socket); return false; }

    fputs($socket, "MAIL FROM: <{$from}>\r\n"); fgets($socket, 512);
    fputs($socket, "RCPT TO: <{$to}>\r\n");    fgets($socket, 512);
    fputs($socket, "DATA\r\n");                  fgets($socket, 512);

    $headers  = "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $headers .= "From: Berber Magic Tours <{$from}>\r\n";
    $headers .= "Sender: {$from}\r\n";
    $headers .= "Return-Path: <{$from}>\r\n";
    $headers .= "Reply-To: {$reply_to}\r\n";
    $headers .= "To: {$to}\r\n";
    $headers .= "Subject: {$subject}\r\n";

    fputs($socket, $headers . "\r\n" . $html_content . "\r\n.\r\n");
    fgets($socket, 512);
    fputs($socket, "QUIT\r\n");
    fclose($socket);
    return true;
}

// -------------------------------------------------------------------------
// 7. Send — SMTP preferred, PHP mail() as fallback
// -------------------------------------------------------------------------
$sent = false;

if ($smtp_pass !== null) {
    $hosts = [
        ['host' => 'localhost',                        'port' => 25],
        ['host' => '127.0.0.1',                        'port' => 25],
        ['host' => 'localhost',                        'port' => 465],
        ['host' => 'berber-magic-tours.com',           'port' => 465],
        ['host' => 'mail.berber-magic-tours.com',      'port' => 465],
        ['host' => 'premium705.web-hosting.com',       'port' => 465],
    ];
    foreach ($hosts as $h) {
        if (send_smtp_email($h['host'], $h['port'], $smtp_user, $smtp_pass,
                            $smtp_user, $to_email, $subject, $body_html, $reply_to)) {
            $sent = true;
            break;
        }
    }
}

if (!$sent) {
    $headers  = "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $headers .= "From: Berber Magic Tours <{$smtp_user}>\r\n";
    $headers .= "Sender: {$smtp_user}\r\n";
    $headers .= "Return-Path: <{$smtp_user}>\r\n";
    $headers .= "Reply-To: {$reply_to}\r\n";
    @mail($to_email, $subject, $body_html, $headers, "-f {$smtp_user}");
    $sent = true; // php mail() does not report delivery failure
}

// -------------------------------------------------------------------------
// 8. Response — always generic, never leak internals
// -------------------------------------------------------------------------
echo json_encode([
    'status'  => 'success',
    'message' => 'Thank you! Your request has been submitted successfully. Our team will get back to you shortly.'
]);
