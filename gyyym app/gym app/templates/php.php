<?php
$host = '127.0.0.1'; // Zmień na odpowiednie dane
$db = 'meowscles';
$user = 'root';
$pass = 'meowsclesgymapp';


$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$user_name = $_POST['user_name'];
$user_password = $_POST['user_password']; // Pamiętaj, aby hasła nie trzymać w czystym tekście
$user_email = $_POST['user_email'];

$sql = "INSERT INTO users (user_name, user_password, user_email) VALUES ('$user_name', '$user_password', '$user_email')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>