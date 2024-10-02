function toggleCategory(category) {
    const container = document.getElementById('categoria-container');
    const tituloCategoria = document.getElementById('titulo-categoria');
    const nombreCategoria = document.getElementById('nombre-categoria');
    const overlay2 = document.getElementById('overlay2');

    if (container.classList.contains('visible')) {
        hideCategory();
    } else {
        tituloCategoria.textContent = category;
        nombreCategoria.textContent = category + '1';

        container.classList.remove('hidden2', 'visuallyhidden2');
        container.classList.add('visible');
        overlay2.classList.add('visible');
    }
}

function hideCategory() {
    const container = document.getElementById('categoria-container');
    const overlay2 = document.getElementById('overlay2');

    container.classList.add('visuallyhidden2');
    overlay2.classList.remove('visible');

    container.addEventListener('transitionend', function (e) {
        container.classList.add('hidden2');
        container.classList.remove('visible');
    }, { once: true });
}