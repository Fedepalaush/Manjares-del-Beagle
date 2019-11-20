function mostrar() {
    document.getElementById('contenedor').style.height = '300px';
    document.getElementById('abrir').style.display = 'none';
    document.getElementById('cerrar').style.display = 'inline';
  }
  
  function ocultar() {
      document.getElementById('contenedor').style.height = '0';
      document.getElementById('abrir').style.display = 'inline';
      document.getElementById('cerrar').style.display = 'none';
  }