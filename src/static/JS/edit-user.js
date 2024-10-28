document.querySelector('.edit-button').addEventListener('click', function () {
    document.querySelector('.edit-button').style.display = 'none';
    document.querySelector('.x').style.display = 'flex';
    document.querySelector('.enviar').classList.add('visible');
    document.querySelector('.enviar').classList.remove('hidden');
    document.getElementById('fijo').classList.add('hidden');
    document.getElementById('fijo2').classList.add('hidden');
    document.getElementById('fijo').classList.remove('visible');
    document.getElementById('fijo2').classList.remove('visible');
    document.getElementById('centrar-user').classList.add('move-center');
    document.getElementById('centrar-user').classList.remove('move-left');
    document.getElementById('Username-label').style.display = 'none';
    document.getElementById('Username-input').style.display = 'flex';
});

document.querySelector('.x').addEventListener('click', function () {
    document.querySelector('.edit-button').style.display = 'flex';
    document.querySelector('.x').style.display = 'none';
    document.querySelector('.enviar').classList.add('hidden');
    document.querySelector('.enviar').classList.remove('visible');
    document.getElementById('fijo').classList.add('visible');
    document.getElementById('fijo2').classList.add('visible');
    document.getElementById('fijo').classList.remove('hidden');
    document.getElementById('fijo2').classList.remove('hidden');
    document.getElementById('centrar-user').classList.add('move-left');
    document.getElementById('centrar-user').classList.remove('move-center');
    document.getElementById('Username-label').style.display = 'flex';
    document.getElementById('Username-input').style.display = 'none';
});
