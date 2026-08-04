// admin.js - Admin panel utilities

document.addEventListener('DOMContentLoaded', () => {
    // Add logic for admin charts or dynamic interactions here if needed
});

// Used in food form for image preview
const imageInput = document.querySelector('input[type="file"][name="image"]');
if(imageInput) {
    imageInput.addEventListener('change', function(e) {
        if(this.files && this.files[0]) {
            // Optional: Show preview
            console.log('Image selected:', this.files[0].name);
        }
    });
}
