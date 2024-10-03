let categoriaGenero = document.getElementById('categoria-genero'),
  categoriaAutor = document.getElementById('categoria-autor'),
  categoriaFecha = document.getElementById('categoria-fecha'),
  container = document.getElementById('categoria-container'),
  icono = document.getElementById('user-icon'),
  exterior_login = document.getElementById('overlay'),
  interior_login = document.getElementById('login-container'),
  subCategorias = document.querySelector('.sub-categorias'),
  categoria = document.querySelector('.categoria'),
  overlay = document.querySelector('.overlay');

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

subCategorias.addEventListener('click', function () {
  console.log('Click en sub-categorias');

  // Toggle visibility of categoria
  if (categoria.classList.contains('hidden')) {
    console.log('Mostrando categoria');
    categoria.classList.remove('hidden');
    setTimeout(function () {
      categoria.classList.remove('visuallyhidden');
      console.log('Categoria visible');
    }, 20);
  } else {
    console.log('Ocultando categoria');
    categoria.classList.add('visuallyhidden');    
    categoria.addEventListener('transitionend', function(e) {
      if (e.propertyName === 'opacity') {
        categoria.classList.add('hidden');
        console.log('Categoria oculta');
      }
    }, { once: true });
  }

  // Toggle visibility of overlay
  if (overlay.classList.contains('hidden')) {
    console.log('Mostrando overlay');
    overlay.classList.remove('hidden');
    setTimeout(function () {
      overlay.classList.remove('visuallyhidden');
      console.log('Overlay visible');
    }, 20);
  } else {
    console.log('Ocultando overlay');
    overlay.classList.add('visuallyhidden');    
    overlay.addEventListener('transitionend', function(e) {
      if (e.propertyName === 'opacity') {
        overlay.classList.add('hidden');
        console.log('Overlay oculto');
      }
    }, { once: true });
  }
}, false);




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
