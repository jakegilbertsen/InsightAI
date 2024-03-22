document.addEventListener('DOMContentLoaded', () => {
    console.log("JavaScript loaded!");

    // Example: Handle form submission
    const form = document.getElementById('data-upload-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            uploadData(this);
        });
    }

    // Function to upload data through AJAX and handle the response
    function uploadData(form) {
        const url = form.action;
        const method = form.method;
        const formData = new FormData(form);

        fetch(url, {
            method: method,
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.success) {
                alert('Data uploaded successfully!');
                // Additional actions like updating the UI or redirecting the user
            } else {
                alert('An error occurred. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please check the console for details.');
        });
    }

    // Dynamic content updates or additional JavaScript functionality
    // can be added here to enhance your application's interactivity.

});

// Additional JavaScript functions or utilities can be defined here.