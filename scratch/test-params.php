<?php
// Simulate POST data directly - test PHP parameter extraction
$_SERVER['REQUEST_METHOD'] = 'POST';
$_POST = [
    'name' => 'Test Client',
    'email' => 'test@test.com',
    'phone' => '+212612345678',
    'date' => '2026-09-15',
    'travelers' => '2',
    'travel_style' => 'Standard',
    'tour_name' => '2 days Mount Toubkal trek',
    'form_type' => 'Tour Booking Request',
    'message' => 'Test reservation - special dietary requirements'
];

// Now include the send-mail logic but just test param extraction
$params = $_POST;

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

echo "=== EXTRACTION TEST ===\n";
echo "Name:      '$name'\n";
echo "Email:     '$email'\n";
echo "Phone:     '$phone'\n";
echo "Date:      '$date'\n";
echo "Travelers: '$travelers'\n";
echo "Style:     '$style'\n";
echo "Tour:      '$tour_name'\n";
echo "Type:      '$form_type'\n";
echo "Message:   '$message'\n";
echo "\nAll OK: " . (!empty($name) && !empty($email) ? "YES" : "NO") . "\n";
