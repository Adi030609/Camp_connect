document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector(".container");
    const sign_in_btn = document.querySelector("#sign-in-btn");
    const sign_up_btn = document.querySelector("#sign-up-btn");
    const signInForm = document.getElementById('signInForm');
    const signUpForm = document.getElementById('signUpForm');
    const popupMessage = document.getElementById('popupMessage');
    const popupText = document.getElementById('popupText');
    const closePopupButton = document.getElementById('closePopupButton'); // Close button

    const users = [
        { username: "admin1", password: "abc123", role: "admin" },
        { username: "admin2", password: "efg123", role: "admin" },
        { username: "faculty1", password: "faculty123", role: "faculty" },
        { username: "student1", password: "student123", role: "student" }
    ];

    // Mouse move event to change background color
    container.addEventListener("mousemove", (e) => {
        const x = e.clientX / window.innerWidth * 100;
        const y = e.clientY / window.innerHeight * 100;

        container.style.setProperty("--bg-color1", `hsl(${x}, 100%, 50%)`);
        container.style.setProperty("--bg-color2", `hsl(${y}, 100%, 50%)`);
    });

    sign_up_btn.addEventListener("click", () => {
        container.classList.add("sign-up-mode");
    });

    sign_in_btn.addEventListener("click", () => {
        container.classList.remove("sign-up-mode");
    });

    signInForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById('signInUsername').value;
        const password = document.getElementById('signInPassword').value;

        const user = users.find(user => user.username === username && user.password === password);
        if (user) {
            showPopup(`Successfully logged in as ${user.role}.`);
            setTimeout(() => {
                if (user.role === "admin") {
                    window.location.href = "admin.html"; 
                } else if (user.role === "faculty") {
                    window.location.href = "faculty.html"; 
                } else {
                    window.location.href = "student.html"; 
                }
            }, 2000); // Redirect after 2 seconds
        } else {
            showPopup("Invalid credentials. Please try again.");
        }
    });

    signUpForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById('signUpUsername').value;
        const email = document.getElementById('signUpEmail').value;
        const password = document.getElementById('signUpPassword').value;

        // Check if user already exists
        if (users.some(user => user.username === username)) {
            showPopup("Username already exists. Please choose another.");
        } else {
            users.push({ username, password, role: "student" }); // Default role as 'student'
            showPopup("Successfully signed up!");
        }
    });

    function showPopup(message) {
        popupText.textContent = message;
        popupMessage.style.display = 'block';
    }

    function closePopup() {
        popupMessage.style.display = 'none';
    }

    // Add event listener to the close button to close the popup
    closePopupButton.addEventListener('click', closePopup); 
});

