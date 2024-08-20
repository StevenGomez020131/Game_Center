var modal = document.getElementById("myModal");
var modalDesc = document.getElementById("modalDescription");
var span = document.getElementsByClassName("close")[0];

// Agregar evento de clic a cada imagen para abrir el modal
document.querySelectorAll('.card_imagen').forEach(function(img) {
    img.onclick = function() {
        modal.style.display = "block";
        modalDesc.textContent = this.dataset.description;
    };
});

// Cuando el usuario haga clic en <span> (x), cierra el modal
span.onclick = function() {
    modal.style.display = "none";
};

// Cuando el usuario haga clic en cualquier parte fuera del modal, lo cierra
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};