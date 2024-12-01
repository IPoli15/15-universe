document.getElementById("cancelarReserva").addEventListener("click", function () {
    const id_reserva = this.getAttribute("data-reserva-id");
    
    document.getElementById("mensaje-exito").style.display = "none";
    document.getElementById("mensaje-error").style.display = "none";
    document.getElementById("aviso").style.display = "none";

    if (!id_reserva) {
        console.error("No se proporcionó un ID de reserva");
        document.getElementById("mensaje-error").style.display = "block";
        document.getElementById("aviso").style.display = "flex";
        return;
    }

    fetch(`http://127.0.0.1:5001/eliminar-reserva/${id_reserva}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            if (response.status === 404) {
                throw new Error("No se encontró una reserva con este ID.");
            }
            throw new Error("Error al eliminar la reserva.");
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        document.getElementById("mensaje-exito").style.display = "block";
        document.getElementById("aviso").style.display = "flex";
    })
    .catch(error => {
        console.error(error);
        document.getElementById("mensaje-error").style.display = "block";
        document.getElementById("aviso").style.display = "flex";
    });

});

function cerrarAviso() {
    document.getElementById("aviso").style.display = "none";
    }
