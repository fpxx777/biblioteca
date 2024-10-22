document.querySelector('.edit-button').addEventListener('click', function () {
    document.querySelector('.edit-button').style.display = 'none';
    document.querySelector('.x').style.display = 'flex';
    document.querySelector('.enviar').style.display = 'flex';
    document.getElementById('icon-gmail').style.display = 'none';
    document.getElementById('icon-date').style.display = 'none';
    document.getElementById('centrar-user').classList.add('move-center');
    document.getElementById('centrar-user').classList.remove('move-left');
});

document.querySelector('.x').addEventListener('click', function () {
    document.querySelector('.edit-button').style.display = 'flex';
    document.querySelector('.x').style.display = 'none';
    document.querySelector('.enviar').style.display = 'none';
    document.getElementById('icon-gmail').style.display = 'block';
    document.getElementById('icon-date').style.display = 'block';
    document.getElementById('centrar-user').classList.add('move-left');
    document.getElementById('centrar-user').classList.remove('move-center');    
});