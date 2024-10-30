let container = document.getElementById('categoria-container'),
    icono = document.getElementById('user-icon'),
    exterior_login = document.getElementById('overlay'),
    interior_login = document.getElementById('login-container'),
    subCategorias = document.querySelectorAll('.sub-categorias'),
    exterior_categoria = document.querySelector('.overlay2'),
    interior_categoria = document.querySelector('.categoria');

let categorias = {};

// Función para cargar las categorías desde el servidor
async function cargarCategorias() {
    try {
        const response = await fetch('/api/categorias');
        categorias = await response.json();
    } catch (error) {
        console.error('Error al cargar las categorías:', error);
    }
}

// Función para mostrar las categorías
function mostrarCategorias(categoria) {
    const tituloCategoria = document.getElementById('titulo-categoria');
    const contenedorCategorias = document.querySelector('.for-nombre-categoria');
    
    // Limpiar contenido anterior
    contenedorCategorias.innerHTML = '';
    
    // Establecer título
    tituloCategoria.textContent = categorias[categoria].titulo;
    
    // Crear y añadir subcategorías
    categorias[categoria].subcategorias.forEach(subcat => {
        const spaceCategoria = document.createElement('div');
        spaceCategoria.className = 'space-categoria';
        
        const titulo = document.createElement('h1');
        titulo.className = 'nombre-categoria';
        titulo.textContent = subcat.nombre;
        
        const lista = document.createElement('div');
        lista.innerHTML = `
            <ul class="lista-categorias">
                ${subcat.opciones.slice(0, 5).map(opcion => `
                    <li><a href="/categoria/${categoria}/${encodeURIComponent(opcion)}">${opcion}</a></li>
                `).join('')}
                <li><a href="/categoria/${categoria}">Ver más ></a></li>
            </ul>
        `;
        
        spaceCategoria.appendChild(titulo);
        spaceCategoria.appendChild(lista);
        contenedorCategorias.appendChild(spaceCategoria);
    });
}

// Event listeners
document.querySelectorAll('.sub-categorias').forEach(item => {
    item.addEventListener('click', () => {
        const categoria = item.dataset.categoria;
        mostrarCategorias(categoria);
        document.querySelector('.categoria').classList.toggle('mostrar');
        document.querySelector('.overlay2').classList.toggle('mostrar');
    });
});

document.querySelector('.overlay2').addEventListener('click', () => {
    document.querySelector('.categoria').classList.remove('mostrar');
    document.querySelector('.overlay2').classList.remove('mostrar');
});

// Cargar las categorías cuando se carga la página
window.addEventListener('load', cargarCategorias);

// Mantener el código existente para el icono de usuario
icono.addEventListener('click', function () {
    // ... (mantener el código existente)
});

exterior_login.addEventListener('click', function () {
    // ... (mantener el código existente)
}); 