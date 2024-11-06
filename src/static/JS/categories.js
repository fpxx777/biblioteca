let container = document.getElementById('categoria-container'),
    icono = document.getElementById('user-icon'),
    exterior_login = document.getElementById('overlay'),
    interior_login = document.getElementById('login-container'),
    subCategorias = document.querySelectorAll('.sub-categorias'),
    exterior_categoria = document.querySelector('.overlay2'),
    interior_categoria_genero = document.getElementById('categoria-container'),
    interior_categoria_autor = document.getElementById('categoria-container2'),
    interior_categoria_fecha = document.getElementById('categoria-container3'),
    firstHover = true,
    activeCategory = null;

icono.addEventListener('click', function () {
    if (interior_login.classList.contains('hidden')) {
        interior_login.classList.remove('hidden');
        setTimeout(function () {
            interior_login.classList.remove('visuallyhidden');
        }, 20);
    } else {
        interior_login.classList.add('visuallyhidden');
        interior_login.addEventListener('transitionend', function (e) {
            if (e.propertyName === 'opacity') {
                interior_login.classList.add('hidden');
            }
        }, { once: true });
    }
    if (exterior_login.classList.contains('hidden')) {
        exterior_login.classList.remove('hidden');
        setTimeout(function () {
            exterior_login.classList.remove('visuallyhidden');
        }, 20);
    } else {
        exterior_login.classList.add('visuallyhidden');
        exterior_login.addEventListener('transitionend', function (e) {
            if (e.propertyName === 'opacity') {
                exterior_login.classList.add('hidden');
            }
        }, { once: true });
    }
}, false);

exterior_login.addEventListener('click', function () {
    interior_login.classList.add('visuallyhidden');
    interior_login.addEventListener('transitionend', function (e) {
        if (e.propertyName === 'opacity') {
            interior_login.classList.add('hidden');
        }
    }, { once: true });
    exterior_login.classList.add('visuallyhidden');
    exterior_login.addEventListener('transitionend', function (e) {
        if (e.propertyName === 'opacity') {
            exterior_login.classList.add('hidden');
        }
    }, { once: true });
}, false);

subCategorias.forEach(item => {
    item.addEventListener('mouseenter', () => {
        let targetId = item.id;

        if (firstHover) {
            if (targetId === 'categoria-genero') {
                interior_categoria_genero.classList.add('mostrar');
                activeCategory = interior_categoria_genero;
            } else if (targetId === 'categoria-autor') {
                interior_categoria_autor.classList.add('mostrar');
                activeCategory = interior_categoria_autor;
            } else if (targetId === 'categoria-fecha') {
                interior_categoria_fecha.classList.add('mostrar');
                activeCategory = interior_categoria_fecha;
            }
            firstHover = false;
        } else {
            if (targetId === 'categoria-genero') {
                activeCategory.style.transition = 'none';
                interior_categoria_genero.style.transition = 'none';
                activeCategory.classList.remove('mostrar');
                interior_categoria_genero.classList.add('mostrar');
                activeCategory = interior_categoria_genero;
            } else if (targetId === 'categoria-autor') {
                activeCategory.style.transition = 'none';
                interior_categoria_autor.style.transition = 'none';
                activeCategory.classList.remove('mostrar');
                interior_categoria_autor.classList.add('mostrar');
                activeCategory = interior_categoria_autor;
            } else if (targetId === 'categoria-fecha') {
                activeCategory.style.transition = 'none';
                interior_categoria_fecha.style.transition = 'none';
                activeCategory.classList.remove('mostrar');
                interior_categoria_fecha.classList.add('mostrar');
                activeCategory = interior_categoria_fecha;
            }
        }
        exterior_categoria.classList.add('mostrar');
    });
});

exterior_categoria.addEventListener('click', () => {
    if (activeCategory) {
        activeCategory.classList.remove('mostrar');
    }
    exterior_categoria.classList.remove('mostrar');
    setTimeout(() => {
        interior_categoria_genero.style.transition = '';
        interior_categoria_autor.style.transition = '';
        interior_categoria_fecha.style.transition = '';
    }, 20);
    firstHover = true;
});

let subCategoriasTop = document.querySelectorAll('.sub-categorias-top');

subCategoriasTop.forEach(item => {
    item.addEventListener('click', () => {
        let targetId = item.id;
        let container;

        if (targetId === 'categoria-genero') {
            container = interior_categoria_genero;
        } else if (targetId === 'categoria-autor') {
            container = interior_categoria_autor;
        } else if (targetId === 'categoria-fecha') {
            container = interior_categoria_fecha;
        }

        if (activeCategory && activeCategory !== container) {
            activeCategory.classList.remove('mostrar');
        }

        if (container.classList.contains('mostrar')) {
            container.classList.remove('mostrar');
            activeCategory = null;
        } else {
            container.classList.add('mostrar');
            activeCategory = container;
        }

        if (exterior_categoria.classList.contains('mostrar')) {
            exterior_categoria.classList.remove('mostrar'); 
        } else { 
            exterior_categoria.classList.add('mostrar'); }
    });
});

exterior_categoria.addEventListener('click', () => {
    if (activeCategory) {
        activeCategory.classList.remove('mostrar');
    }
    exterior_categoria.classList.remove('mostrar');
});




/*
btn.addEventListener('click', function () {
  
  if (box.classList.contains('hidden')) {
    box.classList.remove('hidden');
    setTimeout(function () {
      box.classList.remove('visuallyhidden');
    }, 20);
  } else {
    box.classList.add('visuallyhidden');    
    box.addEventListener('transitionend', function(e) {
      box.classList.add('hidden');
    }, {
      capture: false,
      once: true,
      passive: false
    });
  }
  
}, false);
*/
