document.addEventListener('DOMContentLoaded', function() {
    // Puedes añadir interactividad aquí si es necesario
});

    // Lista de imágenes para el carrusel
    const images = [
        'https://i.ytimg.com/vi/tzhnfcLLrSE/maxresdefault.jpg',
        'https://i.ytimg.com/vi/iqbcJIJGRAs/maxresdefault.jpg',
        'https://via.placeholder.com/800x400/00FF00/FFFFFF?text=Image+3'
    ];

    let currentIndex = 0;

    function showImage(index) {
        const imageElement = document.querySelector('.carousel-image');
        if (index >= images.length) {
            currentIndex = 0; // Vuelve al principio si el índice supera el número de imágenes
        } else if (index < 0) {
            currentIndex = images.length - 1; // Va al final si el índice es menor que 0
        } else {
            currentIndex = index;
        }
        imageElement.src = images[currentIndex];
    }

    function nextImage() {
        showImage(currentIndex + 1);
    }

    function prevImage() {
        showImage(currentIndex - 1);
    }

    // Inicializar con la primera imagen
    showImage(currentIndex);