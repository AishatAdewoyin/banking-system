<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- CSS -->
    <link rel="stylesheet" href="assets/CSS/style.css">
    <link rel="stylesheet" href="assets/CSS/bootstrap.min.css">
    <link rel="stylesheet" href="assets/fonticons/css/all.css">

    <!-- Google fonts APIs -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500&family=Poppins:wght@500&family=Roboto:wght@500&display=swap" rel="stylesheet">


    <title>💵 Investors login</title>
</head>

<body>
    <section class="container">
        <form class="form-login" action="" method="">
            <h2>Welcome Back!</h2>
            <div class="">
                <div class="mb-3">
                    <label for="investors-accName" class="form-label">Your Account Name:</label>
                    <input type="text" class="form-control" id="investors-accName" required aria-describedby="accName">
                    <div id="investors-accName" class="form-text">We'll never share your details with anyone else.</div>
                </div>
                <div class="mb-3">
                    <label for="investors-email" class="form-label">Email address:</label>
                    <input type="email" class="form-control" required id="investors-email" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                    <label for="investors-password" class="form-label">Password:</label>
                    <input type="password" class="form-control"required  id="investors-password">
                </div>
                <div id="i-accName" class="form-link mb-2">Don't have an account? <a href="auth/invest-reg.php">Create Account Here</a></div>
                <button type="submit" class="btn btn-danger">Submit</button>
            </div>
        </form>
    </section>


    <script src="assets/JS/bootstrap.bundle.min.js"></script>
    <script src="assets/JS/index.js"></script>
</body>

</html>