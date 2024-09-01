// Function to toggle between grid and list view
document.getElementById('toggleViewBtn').addEventListener('click', function() {
    const timetable = document.querySelector('.grid-timetable');
    const listTimetable = document.getElementById('listTimetable');

    if (timetable.style.display === 'none') {
        timetable.style.display = 'table'; // Show grid view
        listTimetable.style.display = 'none'; // Hide list view
        this.textContent = 'Switch to List View'; // Change button text
    } else {
        timetable.style.display = 'none'; // Hide grid view
        listTimetable.style.display = 'block'; // Show list view
        this.textContent = 'Switch to Grid View'; // Change button text
    }
});

// Function to send class notifications
function sendClassNotifications() {
    const classElements = document.querySelectorAll('.class');

    classElements.forEach(classElement => {
        const className = classElement.getAttribute('data-class');
        const timeSlot = classElement.parentNode.firstChild.textContent.trim();
        const [startTime, endTime] = timeSlot.split('\n')[1].split(' - ');

        // Convert class start time to Date object
        const classStartTime = new Date();
        const [hours, minutes] = startTime.split(':').map(Number);
        classStartTime.setHours(hours, minutes, 0, 0);

        // Set a timeout to send the notification 5 minutes before class
        const notificationTime = classStartTime.getTime() - (5 * 60 * 1000); // 5 minutes before
        const currentTime = Date.now();

        if (notificationTime > currentTime) {
            const timeUntilNotification = notificationTime - currentTime;
            setTimeout(() => {
                alert(`Reminder: Your class "${className}" starts at ${startTime}.`);
            }, timeUntilNotification);
        }
    });
}

// Call the function to set notifications
sendClassNotifications();