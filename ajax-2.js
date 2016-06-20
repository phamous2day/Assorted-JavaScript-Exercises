// function main() {
//
// }

var mapElm = document.getElementById('map');
var map = new google.maps.Map(mapElm, {
  center: {lat: 33.748995, lng: -84.387982},
  zoom: 4
});
var geocoder = new google.maps.Geocoder();

getGeocode(function(cities, data){
  cities.forEach(function(city) {
    geocoder.geocode({ address: city.name }, function(data) {
      var latLng = data[0].geometry.location;
      var marker = new google.maps.Marker({
        position: latLng,
        map: map
      });
      marker.addListener('click', function() {
        getMarkerInformation(city, function(data){
        getmarkerDetails (data, map, marker);
        });
      });
    });
  });
});





// main();

function getmarkerDetails (data, map, marker) {
  var content = '<h1>' + data.name + '</h1>' +
  'Temperature: ' + data.main.temp + '°<br>' +
  'Hi: ' + data.main.temp_max + '°<br>' +
  'Lo: ' + data.main.temp_min + '°<br>' +
  data.weather[0].description + '<br>' +
  '<img src="http://openweathermap.org/img/w/' + data.weather[0].icon + '.png">';
  var infoWindow = new google.maps.InfoWindow({
    content: content
  });
  infoWindow.open(map, marker);
}

function getMarkerInformation(city, callback) {
  $.ajax({
    url: 'http://api.openweathermap.org/data/2.5/weather',
    method: 'GET',
    data: {
      q: city.name,
      units: 'imperial',
      APPID: 'eac2948bfca65b78a8c5564ecf91d00e'
    },
    success: function(data) {
    callback(data);
      //cut this out, put it in function, put it in function call
    }
  });
}



function getGeocode (callback){
  $.ajax({
    url: 'cities.json',
    success: function(data) {
      callback(data);
    }
  });

}
