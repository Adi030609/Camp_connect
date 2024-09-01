// JavaScript for Menu Toggle
const menuBtn = document.querySelector('.menu-btn');
const menuContent = document.querySelector('.menu-content');

// Toggle Menu Visibility
menuBtn.addEventListener('click', () => {
    menuContent.classList.toggle('show-menu');
});

// Remove the event listener for grid items
document.querySelectorAll('.grid-item a').forEach(item => {
    item.addEventListener('click', function (event) {
        // No need to prevent default; allow redirection
        const url = this.getAttribute('href');
        window.location.href = url; // Redirect to the URL
    });
});