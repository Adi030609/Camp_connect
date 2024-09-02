document.addEventListener("DOMContentLoaded", function() {
    // Handle form submission
    const feedbackForm = document.querySelector('form');

    feedbackForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(feedbackForm);

        fetch('/submit-feedback', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Feedback submitted successfully!');
                feedbackForm.reset();
            } else {
                alert('There was an error submitting your feedback. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting your feedback. Please try again.');
        });
    });
});
