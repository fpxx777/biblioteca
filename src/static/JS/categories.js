let container = document.getElementById('categoria-container'),
  icono = document.getElementById('user-icon'),
  exterior_login = document.getElementById('overlay'),
  interior_login = document.getElementById('login-container'),
  subCategorias = document.querySelector('.sub-categorias'),
  exterior_categoria = document.querySelector('.overlay2'),
  interior_categoria = document.querySelector('.categoria');

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
  if (interior_categoria.classList.contains('hidden2')) {
    interior_categoria.classList.remove('hidden2');
    setTimeout(function () {
      interior_categoria.classList.remove('visuallyhidden2');
    }, 20);
  } else {
    interior_categoria.classList.add('visuallyhidden2');
    interior_categoria.addEventListener('transitionend', function (e) {
      if (e.propertyName === 'opacity') {
        interior_categoria.classList.add('hidden2');
      }
    }, { once: true });
  }

  if (exterior_categoria.classList.contains('hidden2')) {
    exterior_categoria.classList.remove('hidden2');
    setTimeout(function () {
      exterior_categoria.classList.remove('visuallyhidden2');
    }, 20);
  } else {
    exterior_categoria.classList.add('visuallyhidden2');
    exterior_categoria.addEventListener('transitionend', function (e) {
      if (e.propertyName === 'opacity') {
        exterior_categoria.classList.add('hidden2');
      }
    }, { once: true });
  }
}, false);

exterior_categoria.addEventListener('click', function () {
  interior_categoria.classList.add('visuallyhidden2');
  interior_categoria.addEventListener('transitionend', function (e) {
    if (e.propertyName === 'opacity') {
      interior_categoria.classList.add('hidden2');
    }
  }, { once: true });

  exterior_categoria.classList.add('visuallyhidden2');
  exterior_categoria.addEventListener('transitionend', function (e) {
    if (e.propertyName === 'opacity') {
      exterior_categoria.classList.add('hidden2');
    }
  }, { once: true });
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
