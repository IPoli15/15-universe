let selectedRow = null;
const selectButton = document.getElementById("select-btn");

function selectSector(row) {
if (selectedRow) {
    selectedRow.style.backgroundColor = ""; 
}

selectedRow = row;
selectedRow.style.backgroundColor = "#5D2E8C"; 

selectButton.disabled = false;
}

function confirmSelection() {
if (selectedRow) {
    const selectedSector = selectedRow.cells[0].textContent;
    const selectedSectorElement = document.getElementById("selected-sector");

    selectedSectorElement.textContent = `Seleccionaste el sector: ${selectedSector}`;

    selectButton.disabled = true;

    selectedRow.style.backgroundColor = "";
    selectedRow = null;
} else {
    alert("Debes seleccionar un sector.");
}
}