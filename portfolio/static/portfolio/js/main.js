// portfolio/static/portfolio/js/main.js

document.addEventListener('DOMContentLoaded', function () {
    // Select the navigation toggle button and the navigation links container
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    // Check if the toggle button exists
    if (navToggle) {
        navToggle.addEventListener('click', function () {
            // Toggle the 'show' class on the navigation links container
            navLinks.classList.toggle('show');
        });
    }

    // Close the navigation menu if a link is clicked
    navLinks.addEventListener('click', function (event) {
        if (event.target.tagName === 'A') {
            navLinks.classList.remove('show');
        }
    });
});
