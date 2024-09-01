document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const studentName = document.getElementById('studentName').value;
        const studentQuery = document.getElementById('studentQuery').value;
        
        alert(`Thank you, ${studentName}. Your query has been submitted: ${studentQuery}`);
        
        // You can add further logic to handle form submission, like sending data to a server
    });
});
