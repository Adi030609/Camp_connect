// Open and close modals
document.getElementById('changePhotoBtn').addEventListener('click', function() {
    document.getElementById('photoModal').style.display = 'block';
});

document.getElementById('uploadDocumentsBtn').addEventListener('click', function() {
    document.getElementById('documentsModal').style.display = 'block';
});

document.getElementById('closePhotoModal').addEventListener('click', function() {
    document.getElementById('photoModal').style.display = 'none';
});

document.getElementById('closeDocumentsModal').addEventListener('click', function() {
    document.getElementById('documentsModal').style.display = 'none';
});

// Photo upload preview
document.getElementById('photoForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const photoInput = document.getElementById('profilePhotoInput');
    if (photoInput.files.length > 0) {
        const fileName = photoInput.files[0].name;
        document.getElementById('photoPreview').innerHTML = `<p>Uploaded: ${fileName}</p>`;
    }
    document.getElementById('photoModal').style.display = 'none';
});

// Document upload list
document.getElementById('documentsForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const documentInput = document.getElementById('documentInput');
    if (documentInput.files.length > 0) {
        let fileList = '<ul>';
        for (let i = 0; i < documentInput.files.length; i++) {
            fileList += `<li>${documentInput.files[i].name}</li>`;
        }
        fileList += '</ul>';
        document.getElementById('documentsList').innerHTML = `<p>Uploaded:</p> ${fileList}`;
    }
    document.getElementById('documentsModal').style.display = 'none';
});
