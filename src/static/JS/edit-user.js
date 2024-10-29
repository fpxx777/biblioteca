const defaultFile = '/static/img/PhUserCircleFill (1).png';

const file = document.getElementById( 'file' );
const img = document.getElementsByClassName( 'photo' );
file.addEventListener( 'change', e => {
  if( e.target.files[0] ){
    const reader = new FileReader( );
    reader.onload = function( e ){
      img.src = e.target.result;
    }
    reader.readAsDataURL(e.target.files[0])
  }else{
    img.src = defaultFile;
  }
} );

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
    document.querySelector('.foto-user').style.display = 'flex';
    document.querySelector('.visual-foto').style.display = 'none';
    
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
    document.querySelector('.foto-user').style.display = 'none';
    document.querySelector('.visual-foto').style.display = 'flex';
    
});
