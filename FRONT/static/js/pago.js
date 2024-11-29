document.getElementById('paymentForm').addEventListener('submit', function(event) {
    const tickets = document.getElementById('cant_tickets').value;
    if (tickets <= 0) {
        alert('La cantidad de tickets debe ser un número positivo.');
        event.preventDefault();
    }
});