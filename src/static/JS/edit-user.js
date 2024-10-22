document.querySelector('.edit-button').addEventListener('click', function () {
    document.querySelectorAll('.edit-user label, .foto-user label').forEach(label => label.style.display = 'none');
    document.querySelectorAll('.edit-user input, .foto-user input').forEach(input => input.style.display = 'block');
    document.querySelector('.edit-button').style.display = 'none';
    document.querySelector('.x').style.display = 'flex';
    document.querySelector('.enviar').style.display = 'flex';
    document.getElementById('icon-gmail').style.display = 'none';
    document.getElementById('icon-date').style.display = 'none';
});

document.querySelector('.x').addEventListener('click', function () {
    document.querySelectorAll('.edit-user label, .foto-user label').forEach(label => label.style.display = 'block');
    document.querySelectorAll('.edit-user input, .foto-user input').forEach(input => input.style.display = 'none');
    document.querySelector('.edit-button').style.display = 'flex';
    document.querySelector('.x').style.display = 'none';
    document.querySelector('.enviar').style.display = 'none';
    document.getElementById('icon-gmail').style.display = 'block';
    document.getElementById('icon-date').style.display = 'block';
});