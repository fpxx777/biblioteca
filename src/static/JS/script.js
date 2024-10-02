let icono = document.getElementById('user-icon'),
  exterior_login = document.getElementById('overlay'),
  interior_login = document.getElementById('login-container');

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

