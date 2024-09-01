function showSection(sectionId) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('active');
    });

    document.getElementById(sectionId).classList.add('active');
    document.getElementById('current-section').textContent = sectionId.charAt(0).toUpperCase() + sectionId.slice(1);
}

function editProfile() {
    alert("Redirecting to profile edit page...");
    // You can implement redirection or a modal popup for editing profile
}

function viewAcademicHistory() {
    alert("Displaying academic history...");
    // Implement logic to show academic history, maybe in a modal or new page
}

function navigateUniversityHierarchy() {
    alert("Navigating university hierarchy...");
    // Implement hierarchy navigation logic, possibly with interactive charts
}

function bookRoom() {
    alert("Redirecting to room booking...");
    // Redirect to room booking page or open a booking modal
}

function viewDepartmentDetails() {
    alert("Showing department details...");
    // Show detailed department information
}

function viewProgramDetails() {
    alert("Viewing program details...");
    // Display detailed program information
}

function fillExamForm() {
    alert("Filling exam form...");
    // Redirect to exam form fill-up page or open a form modal
}

function registerCourses() {
    alert("Registering for courses...");
    // Handle course registration process
}

function viewTermProgress() {
    alert("Viewing term progression...");
    // Display term-wise progression information
}

function uploadCertificate() {
    alert("Uploading certificate...");
    // Handle certificate upload process
}

function downloadCertificate() {
    alert("Downloading transcript...");
    // Handle transcript download
}

function downloadDegree() {
    alert("Downloading degree certificate...");
    // Handle degree certificate download
}
