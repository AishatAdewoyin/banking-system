// const fullnameField = document.querySelector('#full-name');

// fullnameField.addEventListener("keyup", (event) => {
//     const fullnameValue = event.target.value;

//     if (fullnameValue.length > 0) {
//         fetch('/authentication/fullname_validation/', {
//             method: "POST",
//             body: JSON.stringify({ fullName: fullnameValue })
//         })
//         .then(res => {
//             if (!res.ok) {
//                 throw new Error(`HTTP error! Status: ${res.status}`);
//             }
//             return res.json();
//         })
//         .then(data => {
//             console.log('data', data);
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     }
// });



