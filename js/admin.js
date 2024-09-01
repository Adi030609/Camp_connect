document.getElementById('timetable-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const className = document.getElementById('class-name').value;
    const facultyName = document.getElementById('faculty-name').value;
    const startTime = document.getElementById('start-time').value;
    const endTime = document.getElementById('end-time').value;

    if (checkOverlap(startTime, endTime)) {
        alert('Class timings overlap with an existing class!');
    } else {
        addClassToTimetable(className, facultyName, startTime, endTime);
        alert('Class added successfully!');
    }
});

function checkOverlap(startTime, endTime) {
    const rows = document.querySelectorAll('#timetable tbody tr');
    for (let row of rows) {
        const existingStartTime = row.cells[2].textContent;
        const existingEndTime = row.cells[3].textContent;
        if (
            (startTime >= existingStartTime && startTime < existingEndTime) ||
            (endTime > existingStartTime && endTime <= existingEndTime)
        ) {
            return true;
        }
    }
    return false;
}

function addClassToTimetable(className, facultyName, startTime, endTime) {
    const tableBody = document.querySelector('#timetable tbody');
    const newRow = document.createElement('tr');

    newRow.innerHTML = `
        <td>${className}</td>
        <td>${facultyName}</td>
        <td>${startTime}</td>
        <td>${endTime}</td>
    `;

    tableBody.appendChild(newRow);
}
