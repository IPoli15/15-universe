
const obras = {
    "Jardin japones": {
        img: "static/img/jp/Jardin_jap_3.jpg",
        description: ""
    },
    "Placeholder": {
        img: "static/img/jp/Jardin_jap_1.jpg",
        description: ""
    },
    "Placeholder1": {
        img: "static/img/jp/jardin_jap_2.jpg",
        description: ""
    },
    "Placeholder2": {
        img: "static/img/jp/Jardin_jp_mapa.png",
        description: ""
    }
};

function selectSector(row) {

    const previouslySelected = document.querySelector('.ticket-table .selected');
    if (previouslySelected) {
        previouslySelected.classList.remove('selected');
    }


    row.classList.add('selected');

    const obra = row.cells[0].innerText;
    document.getElementById("event-image").src = obras[obra].img;
    document.getElementById("event-description").innerText = obras[obra].description;

    document.getElementById("select-btn").disabled = false;
}

function confirmSelection() {
    const selectedRow = document.querySelector('.ticket-table .selected');
    if (selectedRow) {
        const selectedText = selectedRow.cells[0].innerText;
        document.getElementById("selected-sector").innerText = `Has seleccionado: ${selectedText}`;
    }
}


