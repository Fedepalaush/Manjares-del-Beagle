function initialize() {
    var input = document.getElementById('searchTextField'); //Trae la info del textField
    var autocomplete = new google.maps.places.Autocomplete(input); //Busca las direcciones
      google.maps.event.addListener(autocomplete, 'place_changed', function () {// Muestra la informacion en el html
          //var place = autocomplete.getPlace();
          //Guardar latitud y longitud en modelo mapa.
      });
}
google.maps.event.addDomListener(window, 'load', initialize);
