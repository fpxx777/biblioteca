let icono = document.getElementById('user-icon'),
    exterior_login = document.getElementById('overlay'),
    interior_login = document.getElementById('login-container');


icono.addEventListener('click', function () {
    interior_login.style.display = 'flex';
    interior_login.style.opacity = '1'
    exterior_login.style.display = 'block';
    exterior_login.style.opacity = '1'
});

exterior_login.addEventListener('click', function () {
    interior_login.style.display = 'none';
    interior_login.style.opacity = '0'
    exterior_login.style.display = 'none';
    exterior_login.style.opacity = '0'
    
});


/*
icono.addEventListener('click', function () {

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

exterior_login.addEventListener('click', function () {
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
