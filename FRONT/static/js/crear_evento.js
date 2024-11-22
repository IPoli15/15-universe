document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const successMessage = document.createElement('div');
    successMessage.classList.add('success-message');
    successMessage.textContent = "Evento creado con éxito";
    successMessage.style.display = 'none';
    form.appendChild(successMessage);

    form.addEventListener('submit', function (event) {
        event.preventDefault(); 

        successMessage.style.display = 'block'; 

        setTimeout(function () {
            form.submit();
        }, 2000); //este es el tiempo que pasa antes que recargue la pagina son 2s
    });
});
