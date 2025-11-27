document.addEventListener("DOMContentLoaded", function() {
    const loader = document.getElementById('loader');
    const autoCompleteInput = document.getElementById('autoComplete');
    const movieButton = document.querySelector('.movie-button');
    const failMessage = document.querySelector('.fail');

    const showLoader = () => loader.style.display = 'block';
    const hideLoader = () => loader.style.display = 'none';

    autoCompleteInput.addEventListener('input', function() {
        // Enable or disable the button based on input
        movieButton.disabled = !this.value.trim();
    });

    movieButton.addEventListener('click', function() {
        showLoader();
        failMessage.style.display = 'none'; // Hide fail message if it was shown

        // Fetch recommendations
        fetch('/similarity', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ name: autoCompleteInput.value })
        })
        .then(response => response.text())
        .then(data => {
            hideLoader();
            if (data.startsWith("Sorry!")) {
                failMessage.innerHTML = data;
                failMessage.style.display = 'block';
            } else {
                // Handle successful recommendation display (you can modify this as needed)
                alert('Recommendations: ' + data);
            }
        })
        .catch(error => {
            hideLoader();
            console.error('Error:', error);
        });
    });
});
