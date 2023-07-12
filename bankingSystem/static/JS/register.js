// $(document).ready(function() {
//     $(".hero").addClass("h1-animate h4-animate p-animate");
//   });


// document.getElementById('registration-form').addEventListener('submit', function(event) {
//     event.preventDefault(); // Prevent form submission

//     var form = event.target;
//     var validationMessage = document.getElementById('validation-message');

//     // Validate form fields
//     if (!form.checkValidity()) {
//         validationMessage.textContent = 'Please fill out all required fields.';
//         validationMessage.className = 'alert error';
//         return;
//     }

//     // Form submission is successful
//     validationMessage.textContent = 'Form submitted successfully!';
//     validationMessage.className = 'alert success';

//     // Further actions (e.g., AJAX submission)
//     // ...
// });

const fullnameField = document.querySelector('#full-name');

fullnameField.addEventListener("keyup", (event) => {
    console.log('7777777');

    const fullnameValue = event.target.value;

    if (fullnameValue.length > 0) {
        fetch('/authentication/fullname_validation/', {
            method: "POST",
            body: JSON.stringify({ fullName: fullnameValue })
        }).then(res => res.json())
        .then(data => {
            console.log('data', data);
        });
    }
});


