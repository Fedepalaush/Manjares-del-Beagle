
//Iniciamos el mapa con los marcadores del JSON




function initMap(){
  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 13,
    center: {lat:-54.8161769 ,lng: -68.3278668}
  });

  var informacion = new google.maps.InfoWindow();


var markers = []
for (var i=0; i<markersData.length; i++){
    var marker = new google.maps.Marker({
      position: {lat:markersData[i].lat ,lng: markersData[i].long},
      map: map,
      data: markersData[i]
    });

    marker.addListener('click', function(){
        var content = '<h3>' + this.data.dir + '</h3>' +
          '<p>Pedido N°XXXXXX</p>' +
          '<button type="button">Detalles</button>' +
          '<button type="button">Entregado</button>';
        informacion.setContent(content)
        informacion.open(map, this);
    });

    markers.push(marker)
 }


    //TRAZANDO EL CAMINO ENTRE EN MARCADOR 1 Y 2
    var objConfigDR = {
        map: map,
        suppressMarkers: true,
        sensor: false
    }
    var objConfigDS = {
        origin: markers[0].position, //Lat o Long - String
        destination: markers[1].position,
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

    //Se recorre un JSON para agregar marcadores
}