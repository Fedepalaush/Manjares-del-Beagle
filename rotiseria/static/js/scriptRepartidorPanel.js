
function mostrar() {
  document.getElementById('contenedor').style.height = '300px';
  document.getElementById('abrir').style.display = 'none';
  document.getElementById('cerrar').style.display = 'inline';
  document.getElementById('imagenMapa').src = 'http://maps.googleapis.com/maps/api/streetview?size=160x205&location='+ document.getElementById('latitud').value +','+ document.getElementById('longitud').value +'&sensor=false&key=AIzaSyC5bJ7e24SdcnhOtbqPMfC30MrOlhLyMTI';
}

function ocultar() {
  document.getElementById('contenedor').style.height = '0';
  document.getElementById('abrir').style.display = 'inline';
  document.getElementById('cerrar').style.display = 'none';
}