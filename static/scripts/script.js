/*
    API
    Define the API endpoint
*/
/* const apiUrl = 'https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={e412a82b}&app_key={ec6c5b91815afb492dd48b5a66af3314}';

// Function to make the API request and update the HTML
async function fetchData() {
    try {
        const response = await fetch('https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id={e412a82b}&app_key={ec6c5b91815afb492dd48b5a66af3314}');
        if (response.ok) {
            const data = await response.json();
            // Update the HTML element with the API data
            const apiDataElement = document.getElementById('api-data');
            apiDataElement.innerHTML = JSON.stringify(data, null, 2);
        } else {
            console.error('API request failed');
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
}
// Call the fetchData function when the page loads
window.addEventListener('load', fetchData); */

/* Java HTML script if used 
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div id="api-data"></div>
    <script src="script.js"></script>
</body>
</html>
Define the API endpoint */

// Dropdown Functions
console.log("Loaded")
const dropdownButton = document.getElementById("dropdown-btn");

if (dropdownButton) {
    dropdownButton.addEventListener('click', () => {
        const dropdownToActive = document.getElementById("dropdown-content")
        dropdownToActive.classList.toggle("active")
    })

    document.addEventListener('click', (e) => {
        const dropdownContent = document.getElementById('dropdown-content');

        if (!e.target.closest('#dropdown-btn') && !e.target.closest('#dropdown-content')) {
        dropdownContent.classList.remove('active');
        }
    });
}

// Login Functions
const registerButton = document.getElementById("register-button");
const loginButton = document.getElementById("login-button");

if (registerButton || loginButton) {
    registerButton.addEventListener('click', () => {
        const leftContainer = document.getElementById("left-container");
        const rightContainer = document.getElementById("right-container");
        const loginBlock = document.getElementById("login-block");
        const registerBlock = document.getElementById("register-block");


        leftContainer.classList.toggle("active");
        rightContainer.classList.toggle("active");
        loginBlock.classList.toggle("active");
        registerBlock.classList.toggle("active");
        registerButton.classList.toggle("active");
        loginButton.classList.toggle("active");
    })

    loginButton.addEventListener('click', () => {
        const leftContainer = document.getElementById("left-container");
        const rightContainer = document.getElementById("right-container");
        const loginBlock = document.getElementById("login-block");
        const registerBlock = document.getElementById("register-block");


        leftContainer.classList.toggle("active");
        rightContainer.classList.toggle("active");
        loginBlock.classList.toggle("active");
        registerBlock.classList.toggle("active");
        registerButton.classList.toggle("active");
        loginButton.classList.toggle("active");
    })
}