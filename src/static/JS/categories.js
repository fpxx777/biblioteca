let categoriaGenero = document.getElementById('categoria-genero'),
    categoriaAutor = document.getElementById('categoria-autor'),
    categoriaFecha = document.getElementById('categoria-fecha'),
    overlay = document.getElementById('overlay2'),
    container = document.getElementById('categoria-container');

function toggleVisibility() {
    if (overlay.classList.contains('hidden2')) {
        overlay.classList.remove('hidden2');
        container.classList.remove('hidden2');
        setTimeout(function () {
            overlay.classList.remove('visuallyhidden2');
            container.classList.remove('visuallyhidden2');
        }, 20);
    } else {
        overlay.classList.add('visuallyhidden2');
        container.classList.add('visuallyhidden2');
        overlay.addEventListener('transitionend', function(e) {
            if (e.target === overlay) {
                overlay.classList.add('hidden2');
                container.classList.add('hidden2');
            }
        }, {
            capture: false,
            once: true,
            passive: false
        });
    }
}

categoriaAutor.addEventListener('click', toggleVisibility);
categoriaFecha.addEventListener('click', toggleVisibility);
categoriaGenero.addEventListener('click', toggleVisibility);

document.addEventListener('DOMContentLoaded', function() {
    overlay.classList.add('hidden2');
    container.classList.add('hidden2');
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
