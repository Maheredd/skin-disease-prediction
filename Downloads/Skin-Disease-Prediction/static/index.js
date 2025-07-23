// Trigger file selection when clicking the drop area
document.getElementById('drop-area').addEventListener('click', () => {
    document.getElementById('file-input').click();
});

// When a file is selected, preview the image
document.getElementById('file-input').addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        previewImage(file);
    }
});

// Allow image pasting (Ctrl+V)
document.addEventListener('paste', (event) => {
    const items = (event.clipboardData || event.originalEvent.clipboardData).items;
    for (const item of items) {
        if (item.kind === 'file') {
            const file = item.getAsFile();
            previewImage(file);
            break;
        }
    }
});

// Preview image in the <img> tag
function previewImage(file) {
    const img = document.getElementById('preview');
    const reader = new FileReader();
    reader.onload = (e) => {
        img.src = e.target.result;
        img.style.display = 'block';
    };
    reader.readAsDataURL(file);
}
