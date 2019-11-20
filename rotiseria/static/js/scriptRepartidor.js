//Iniciamos el mapa con los marcadores del JSON

function initMap(){
  var ushuaia = {lat:-54.8161769 ,lng: -68.3278668};
  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 13,
    center: ushuaia
  });

  //agrego letras a los marcadores
  var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  var labelIndex = 0;

  //MARCADOR DE INICIO ESTATICO - MANJARES DEL BEAGLE
  var markerInicio = new google.maps.Marker({
    position: {lat: -54.809196,lng: -68.3141325},
    label: labels[labelIndex++ % labels.length],
    map: map
  });
  markerInicio.addListener('click', function(){
    var content = '<h3>' + 'Gral. Manuel Belgrano 43' + '</h3>' +
      '<p> Manjares del Beagle </p>';
      informacion.setContent(content);
      informacion.open(map, this);
    });

  var informacion = new google.maps.InfoWindow();

  //ARREGLO DE MARCADORES
  var markers = [];
  //AGREGO EL MARCADOR DE INICIO
  markers.push(markerInicio);
  for (var i=0; i<markersData.length; i++){
    //MARKER: UN MARCADOR
    var marker = new google.maps.Marker({
      position: {lat:markersData[i].lat ,lng: markersData[i].long},
      label: labels[labelIndex++ % labels.length],
      map: map,
      data: markersData[i]
    });
    marker.addListener('click', function(){
      var content = '<h3>' + this.data.dir + '</h3>' +
        '<p>Pedido N°XXXXXX</p>' +
        '<button type="button" id="abrir" href="javascript:void(0)" onclick="mostrar()">Detalles</button>' +
        '<button type="button">Entregado</button>';
        informacion.setContent(content);
        informacion.open(map, this);
      });
    markers.push(marker)
  }

  

  //TRAZANDO EL CAMINO ENTRE EL MARCADOR INICIO -- (marcadores de por medio) -- FIN
  var objConfigDR = {
    map: map,
    suppressMarkers: true,
    sensor: false
  }

  var waypoints = [];
  for (let index = 1; index < markers.length-1; index++) {
    waypoints.push({location: markers[index].position, stopover: false});
  };
    
  var objConfigDS = {
      origin: markers[0].position, //Lat o Long - String
      destination: markers[markers.length-1].position,
      waypoints: waypoints,
      travelMode: google.maps.TravelMode.DRIVING
  }

  var ds = new google.maps.DirectionsService(); //obtiene las coordenadas
  var dr = new google.maps.DirectionsRenderer(objConfigDR); //traduce coordenadas a la ruta visible

  ds.route(objConfigDS, fnRutear);
  function fnRutear(resultados, status) {
      if (status == 'OK'){
          dr.setDirections(resultados);
      } else {
          alert('Error: ' + status);
      }
  }
  
}