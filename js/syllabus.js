function openTab(event, tabName) {
    // Get all tab contents and hide them
    var tabContents = document.getElementsByClassName("tab-content");
    for (var i = 0; i < tabContents.length; i++) {
        tabContents[i].classList.remove("active");
    }

    // Get all tab buttons and remove the active class
    var tabButtons = document.getElementsByClassName("tab-button");
    for (var i = 0; i < tabButtons.length; i++) {
        tabButtons[i].classList.remove("active");
    }

    // Show the clicked tab's content and set the button to active
    document.getElementById(tabName).classList.add("active");
    event.currentTarget.classList.add("active");
}
