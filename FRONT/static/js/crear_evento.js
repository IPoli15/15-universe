document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const successMessage = document.getElementById('successMessage'); 

    form.addEventListener('submit', function (event) {
        event.preventDefault(); 

        successMessage.style.display = 'block';

        setTimeout(function () {
            successMessage.style.display = 'none';
        }, 6000);
    });
});
