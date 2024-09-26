document.getElementById('user-icon').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('login-container').style.display = 'block';
});

document.getElementById('overlay').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('login-container').style.display = 'none';
});