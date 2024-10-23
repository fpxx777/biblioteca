document.querySelector('.edit-button').addEventListener('click', function () {
    document.querySelector('.edit-button').style.display = 'none';
    document.querySelector('.x').style.display = 'flex';
    document.querySelector('.enviar').style.display = 'flex';
    document.getElementById('fijo').style.display = 'none';
    document.getElementById('fijo2').style.display = 'none';
    document.getElementById('centrar-user').classList.add('move-center');
    document.getElementById('centrar-user').classList.remove('move-left');
    document.getElementById('Username-label').style.display = 'none';
    document.getElementById('Username-input').style.display = 'flex';

});

document.querySelector('.x').addEventListener('click', function () {
    document.querySelector('.edit-button').style.display = 'flex';
    document.querySelector('.x').style.display = 'none';
    document.querySelector('.enviar').style.display = 'none';
    document.getElementById('fijo').style.display = 'block';
    document.getElementById('fijo2').style.display = 'block';
    document.getElementById('centrar-user').classList.add('move-left');
    document.getElementById('centrar-user').classList.remove('move-center');  
    document.getElementById('Username-label').style.display = 'flex';
    document.getElementById('Username-input').style.display = 'none';  
});