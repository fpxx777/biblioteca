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

document.querySelectorAll('.sub-categorias').forEach(item => {
  item.addEventListener('click', () => {
      document.querySelector('.categoria').classList.toggle('mostrar');
      document.querySelector('.overlay2').classList.toggle('mostrar');
  });
});

document.querySelector('.overlay2').addEventListener('click', () => {
  document.querySelector('.categoria').classList.remove('mostrar');
  document.querySelector('.overlay2').classList.remove('mostrar');