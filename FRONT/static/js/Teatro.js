
const obras = {
    "Cascanueces": {
        img: "Cascanueces1.jpg",
        description: "El Centro Nacional de las Artes Delia Zapata Olivella (CNA) confirmo que el mitico Teatro Colon Llegara una de las obras mas importantes del compositor ruso Piotr Ilich Tchaikovsky."
    },
    "Orquesta estable": {
        img: "Orquesta_estable.jpg",
        description: "La orquesta estable dirigida por Gustavo Fontana se presenta en el Teatro Colon, se interpretaran las Danzas Polovtsianas de El principe Igor de Borodin y la Quinta Sinfonia de Tchaikovsky."
    },
    "Moliendo a Moliere": {
        img: "Moliendo_moliere.jpg",
        description: "Espectaculo sobre textos de Moliere y musica de Jean-Baptiste Lully, la obra pone en escena a compañia de artistas, de dudosa reputacion, que se embarca en una mision disparatada para mejorar su situacion."
    },
    "El lago de los cisnes": {
        img: "Lago_cisnes.jpg",
        description: "En el Teatro Colon se presenta el reestreno de El lago de los cisnes con Mario Galizzi. Entre otros bailaran Marianela Nuñez. la rusa Natalia Osipova y el italiano Roberto Bolle."
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



