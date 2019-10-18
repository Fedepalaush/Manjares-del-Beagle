
//Iniciamos el mapa con los marcadores del JSON
function initMap(){
    
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 13,
      center: {lat:-54.8161769 ,lng: -68.3278668}
    });



    //MARCADOR 1
    var marker1 = new google.maps.Marker({
      position: {lat:-54.8161769 ,lng: -68.3278668},
      map: map,
      title: 'Kuanip 189'
    });
    //GLOBO DE INFORMACION DEL MARCADOR 1
    var texto1 = '<h3> Kuanip 189 </h3>' + '<p> Pedido N°210 </p>' + 
                '<input type="button" value="Detalles">';
    var informacion1 = new google.maps.InfoWindow({
        content: texto1
    });
    marker1.addListener('click', function(){
        informacion1.open(map,marker1);
    });


    //MARCADOR 2
    var marker2 = new google.maps.Marker({
      position: {lat:-54.8069544 ,lng: -68.316321},
      map: map,
      title: 'Hernando de Magallanes 1120'
    });
    //GLOBO DE INFORMACION DEL MARCADOR 2
    var texto2 = '<h3> Hernando de Magallanes 1120 </h3>' + '<p> Pedido N°211 </p>' + 
                '<input type="button" value="Detalles">';
    var informacion2 = new google.maps.InfoWindow({
        content: texto2
    });
    marker2.addListener('click', function(){
        informacion2.open(map,marker2);
    });


    //TRAZANDO EL CAMINO ENTRE EN MARCADOR 1 Y 2
    var objConfigDR = {
        map: map,
        suppressMarkers: true,
        sensor: false
    }
    var objConfigDS = {
        origin: marker1.position, //Lat o Long - String
        destination: marker2.position,
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