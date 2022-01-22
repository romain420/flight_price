let map;

function initMap() {
  var map = new google.maps.Map(document.getElementById("home_map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}