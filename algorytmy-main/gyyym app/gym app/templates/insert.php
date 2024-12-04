<!DOCTYPE html>
<html>

<head>
    <title>Insert Page</title>
</head>

<body>
        <?php

        $conn = mysqli_connect("localhost", "root", "meowsclesgymapp", "meowscles");

        // Check connection
        if($conn === false){
            die("ERROR: Could not connect. "
                . mysqli_connect_error());
        }

        // Taking all values from the form data(input)
        $user_name =  $_REQUEST['user_name'];
        $user_password = $_REQUEST['user_password'];
        $user_email = $_REQUEST['user_email'];

        // Performing insert query execution
        // here our table name is college
        $sql = "INSERT INTO college  VALUES ('$user_name',
            '$user_password','$user_email')";

        if(mysqli_query($conn, $sql)){
            echo "successfully.";

            echo nl2br("\n$user_name\n $user_password\n "
                . "$user_email\n");
        } else{
            echo "ERROR $sql. "
                . mysqli_error($conn);
        }

        // Close connection
        mysqli_close($conn);
        ?>
</body>

</html>
