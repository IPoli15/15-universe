const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('evento_creado') === '1') {
            const successMessage = document.getElementById('successMessage');
            successMessage.style.display = 'block';

            // Ocultar el mensaje despues de 6 segundos
            setTimeout(() => {
                successMessage.style.display = 'none';
            }, 6000); 
        }
