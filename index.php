<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- CSS -->
    <link rel="stylesheet" href="assets/CSS/style.css">
    <link rel="stylesheet" href="assets/CSS/bootstrap.min.css">
    <link rel="stylesheet" href="assets/fonticons/css/all.css">

    <!-- Google fonts APIs -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500&family=Poppins:wght@500&family=Roboto:wght@500&display=swap" rel="stylesheet">


    <title>💵TBNK Banking Plc</title>
</head>

<body>
    <header>
        <!-- Navbar start -->
        <?php
        include_once "services/navbar.php";
        ?>
        <!-- Nav ends-->

        <!-- headimg start -->
        <section class="container text-center" id="herosection">
            <div class="hero">
                <h4 class="text-success mt-3 mb-3">Hi! Welcome to TBNK</h4>
                <h1>We are well known for giving our customers the best solutions for their business growth</h1>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam reprehenderit ducimus quas minima
                    similique laudantium delectus fugiat? Pariatur, hic reprehenderit?</p>
                <div class="mt-5">
                    <button class="me-4"><a href="#">Create an Account</a></button>
                    <button><a href="#">Login to your Account</a></button>
                </div>
            </div>
        </section>
    </header>
    <main>
        <section class="container text-center mb-5" id="services">
            <div class="container text-center services">
                <h2>Our Services</h2>
                <div class="row row-cols-1 row-cols-lg-3 row-cols-md-3 g-3 g-lg-5 g-md-5 my-5">
                    <div class="col icon-box m-3">
                        <div>
                            <i class="fas fa-hand-holding-usd"></i>
                            <h5>Open a Personal Account with us</h5>
                            <p>Start building a healthy savings habit with our Personal Savings Account. It's designed to empower you to save and manage your finances effectively. With this account, you can easily make transactions, track your progress, and watch your savings grow</p>
                        </div>
                    </div>
                    <div class="col icon-box m-3">
                        <div>
                            <i class="fas fa-dollar-sign"></i>
                            <h5>Open a Business Account with us</h5>
                            <p>Take control of your business finances and boost profitability with our secure and convenient Business Account. Manage transactions, track expenses, and maximize your earnings effortlessly. Empower your business to thrive with our tailored financial solutions.</p>
                        </div>
                    </div>
                    <div class="col icon-box m-3">
                        <div>
                            <i class="fas fa-wallet"></i>
                            <h5>Go into Investment with us</h5>
                            <p>Looking to earn as an investor? Invest with us and unlock your earning potential. Our proven investment strategies and expert guidance will help you grow your wealth. Take the first step towards financial success and start earning with us today.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="about" class="container about">
            <div class="container">
                <div class="container design p-5">
                    <h2>About Us</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestiae velit qui aliquam.
                        Dolorem enim et, numquam natus impedit voluptates voluptatibus temporibus error eveniet
                        perferendis iure molestiae quidem consequatur, dolor, doloremque maxime similique quae
                        aliquam blanditiis fugiat voluptas suscipit facilis tenetur non! Unde omnis dignissimos, et
                        nulla perspiciatis officiis saepe consequuntur. Nostrum praesentium, tempora quia et magnam
                        ipsa sed. Voluptate dolor commodi fuga. Similique maiores commodi non delectus nisi amet
                        quibusdam. Iste, animi recusandae! Et commodi eaque dolorem provident ipsum, deserunt
                        obcaecati quisquam voluptatibus nulla fuga! commodi!</p>
                    <img src="assets/images/laptop-graph.jpg" alt="">
                </div>
            </div>
        </section>
        <section id="contact" class="container contact text-center my-5">
            <h2 class="py-4">Contacts</h2>
            <div class=" row row-cols-1 container">
                <div class="col-lg-6 contactdiv text-start">
                    <h5>Social Media:</h5>
                    <ul class="social d-flex">
                        <li><a href="#"><i class="fab fa-facebook-square"></i></a></li>
                        <li><a href="#"><i class="fab fa-instagram-square"></i></a></li>
                        <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                        <li><a href="#"><i class="fab fa-linkedin"></i></a></li>
                    </ul>
                    <h5>Other Details:</h5>
                    <ul class="others d-flex">
                        <li><a href="#"><i class="fas fa-phone"></i> +2347-012-345-6789</a></li>
                        <li><a href="#"><i class="fas fa-envelope-open-text"></i> support@tbnkplc.com</a></li>
                    </ul>
                    <h4>Direction</h4>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31516.474495094226!2d7.378260755297581!3d9.103847596882396!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x104e756e877080fb%3A0xa9cbe3f96accde4e!2sGwarinpa%20Estate%20900108%2C%20Abuja%2C%20Federal%20Capital%20Territory!5e0!3m2!1sen!2sng!4v1686396914611!5m2!1sen!2sng" width="520" height="200" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
                <div class="col-lg-6 text-start">
                    <div class="text-start">
                        <form action="" method="post">
                            <label for="exampleFormControlInput1" class="form-label">Full Name:</label>
                            <input type="text" class="form-control mb-3" id="exampleFormControlInput1" placeholder="Full Name">
                            <label for="exampleFormControlInput2" class="form-label">Email Address:</label>
                            <input type="email" class="form-control mb-3" id="exampleFormControlInput2" placeholder="name@example.com">
                    </div>
                    <div class="mb-3">
                        <label for="exampleFormControlTextarea1" class="form-label">Your Message:</label>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Write your message"></textarea>
                    </div>
                    <div class="d-grid gap-2 col-6 mx-auto">
                        <button class="btn btn-danger" type="submit">Send Message</button>
                    </div>
                    </form>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <div class="">
            <p>All Rights Reserved, <span class="tbnkfoot">💵TBNK PLC</span> <sup>&#169</sup> 2024. Developed By<span class="mylink"><a href="https://github.com/Aishat452" target="_blank"> Aishat Adewoyin</a></span></p>
        </div>
    </footer>
    <script src="assets/JS/bootstrap.bundle.min.js"></script>
    <script src="assets/JS/index.js"></script>
</body>

</html>