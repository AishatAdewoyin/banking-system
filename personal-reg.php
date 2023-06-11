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


    <title>💵 Personal Account Registration</title>
</head>

<body>
    <section class="container reg-form-section">
        <form class="row g-3 form-reg" action="" method="">
            <h2>Account Registration</h2>
            <div class="col-md-12">
                <label for="full-name" class="form-label">Full Name:</label>
                <input type="text" name="fname" class="form-control" required id="full-name" placeholder="Harrison Paul Martins">
            </div>
            <div class="col-md-6">
                <label for="reg-email" class="form-label">Email Adress:</label>
                <input type="email" name="email"class="form-control" required id="reg-email">
            </div>
            <div class="col-md-6">
                <label for="reg-password" class="form-label">Password:</label>
                <input type="password" name="password" placeholder="Abc123@# (Letters,Numbers, and symbols required. Not more then 18 characters)" required class="form-control" maxlength="18" pattern="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$" id="reg-password">
            </div>
            <div class="col-12">
                <label for="reg-address" class="form-label">Address:</label>
                <input type="text" name="address"class="form-control" required id="reg-address" placeholder="No 1, Main St">
            </div>
            <div class="col-12">
                <label for="address2" class="form-label">Address 2:</label>
                <input type="text" name="address2" class="form-control" id="address2" placeholder="Apartment, studio, or floor">
            </div>
            <div class="col-md-6">
                <label for="reg-city" class="form-label">City:</label>
                <input type="text" name="city" class="form-control" id="reg-city">
            </div>
            <div class="col-md-4">
                <label for="reg-state" class="form-label">State:</label>
                <select id="reg-state" name="state" class="form-select">
                    <option selected>Choose...</option>
                    <option value="Abia">Abia</option>
                    <option value="Adamawa">Adamawa</option>
                    <option value="Akwa Ibom">Akwa Ibom</option>
                    <option value="Anambra">Anambra</option>
                    <option value="Bauchi">Bauchi</option>
                    <option value="Bayelsa">Bayelsa</option>
                    <option value="Benue">Benue</option>
                    <option value="Borno">Borno</option>
                    <option value="Cross River">Cross River</option>
                    <option value="Delta">Delta</option>
                    <option value="Ebonyi">Ebonyi</option>
                    <option value="Edo">Edo</option>
                    <option value="Ekiti">Ekiti</option>
                    <option value="Enugu">Enugu</option>
                    <option value="FCT">Federal Capital Territory</option>
                    <option value="Gombe">Gombe</option>
                    <option value="Imo">Imo</option>
                    <option value="Jigawa">Jigawa</option>
                    <option value="Kaduna">Kaduna</option>
                    <option value="Kano">Kano</option>
                    <option value="Katsina">Katsina</option>
                    <option value="Kebbi">Kebbi</option>
                    <option value="Kogi">Kogi</option>
                    <option value="Kwara">Kwara</option>
                    <option value="Lagos">Lagos</option>
                    <option value="Nasarawa">Nasarawa</option>
                    <option value="Niger">Niger</option>
                    <option value="Ogun">Ogun</option>
                    <option value="Ondo">Ondo</option>
                    <option value="Osun">Osun</option>
                    <option value="Oyo">Oyo</option>
                    <option value="Plateau">Plateau</option>
                    <option value="Rivers">Rivers</option>
                    <option value="Sokoto">Sokoto</option>
                    <option value="Taraba">Taraba</option>
                    <option value="Yobe">Yobe</option>
                    <option value="Zamfara">Zamfara</option>
                </select>
            </div>
            <div class="col-md-2">
                <label for="zipcode" class="form-label">Zip Code:</label>
                <input type="text" name="zipcode" class="form-control" id="zipcode">
            </div>
            <div id="i-accName" class="form-link mb-2">Already have an account? <a href="personal-login.php">Login Here</a></div>
            <div class="col-12">
                <button type="submit" class="btn btn-danger">Create an Account</button>
            </div>
        </form>
    </section>


    <script src="assets/JS/bootstrap.bundle.min.js"></script>
    <script src="assets/JS/index.js"></script>
</body>

</html>