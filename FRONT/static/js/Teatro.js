function selectSector(row) {
    const previouslySelected = document.querySelector('.ticket-table .selected');
    if (previouslySelected) {
        previouslySelected.classList.remove('selected');
    }

    row.classList.add('selected');

    const imgSrc = row.cells[0].getAttribute('data-img');
    const description = row.cells[0].getAttribute('data-description');
    document.getElementById("event-image").src = imgSrc;
    document.getElementById("event-description").innerText = description;

    document.getElementById("select-btn").disabled = false;
}

function confirmSelection() {
    const selectedRow = document.querySelector('.ticket-table .selected');
    if (selectedRow) {
        const selectedText = selectedRow.cells[0].innerText;
        document.getElementById("selected-sector").innerText = `Has seleccionado: ${selectedText}`;
    }
}



