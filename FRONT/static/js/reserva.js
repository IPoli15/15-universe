function validarReserva() {
    const id = document.getElementById("idReserva").value;
    const usuario = document.getElementById("usuario").value;

    fetch(`/validarReserva?id=${id}&usuario=${usuario}`)
        .then(response => response.json())
        .then(data => {
            if (data.valido) {
                window.location.href = "/tu-reserva";
            } else {
                alert("Error: ID o usuario inválido.");
            }
        })
        .catch(error => {
            alert("Error de conexión.");
        });
}


