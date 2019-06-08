// Map Code Starts Here
var geocoder = new google.maps.Geocoder();
var positionStore;
var lat;
var lng;
var address;

function geocodePosition(pos) {
    geocoder.geocode({
        latLng: pos
    }, function(responses) {
        if (responses && responses.length > 0) {
            updateMarkerAddress(responses[0].formatted_address);
        } else {
            updateMarkerAddress('Cannot determine address at this location.');
        }
    });
}

function updateMarkerPosition(latLng) {
    lat = latLng.lat();
    lng = latLng.lng();
}

function updateMarkerAddress(str) {
      $('#searchTextField').val(str);
      $('#locationSearch').val(str);
      $('#userAddress').val(str);
      $("#searchTextField").addClass("form-control");
      address = str;
}

function initialize(position) {
    var latLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    var map = new google.maps.Map(document.getElementById('mapCanvas'), {
        zoom: 17,
        center: latLng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        streetViewControl: false,
        mapTypeControl: false
    });
    // Construct the circle for each value in citymap.
    // Note: We scale the area of the circle based on the population.
    var cityCircle = new google.maps.Circle({
        strokeColor: '#03b94d',
        strokeOpacity: 0.5,
        strokeWeight: 1,
        fillColor: '#03b94d',
        fillOpacity: 0.05,
        map: map,
        center: {
            lat: 12.915261,
            lng: 77.604482
        },
        radius: 7000
    });
    var userInfoWindow = new google.maps.InfoWindow({
        content: '<h5>Your Location</h5><p>Drag this to your exact location'
    });
    var userMarker = new google.maps.Marker({
        position: latLng,
        map: map,
        title: 'Your Location',
        animation: google.maps.Animation.DROP,
        draggable: true
    });
    userMarker.addListener('click', function() {
        userInfoWindow.open(map, userMarker);
    });
    var input = document.getElementById('searchTextField');
    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);
    // Update current position info.
    updateMarkerPosition(latLng);
    geocodePosition(latLng);
    // Add dragging event listeners.
    google.maps.event.addListener(userMarker, 'dragstart', function() {
        updateMarkerAddress('Dragging...');
    });
    google.maps.event.addListener(userMarker, 'drag', function() {
        updateMarkerPosition(userMarker.getPosition());
    });
    google.maps.event.addListener(userMarker, 'dragend', function() {
        geocodePosition(userMarker.getPosition());
    });
    google.maps.event.addListener(autocomplete, 'place_changed', function() {
        input.className = '';
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            // Inform the user that the place was not found and return.
            input.className = 'notfound';
            return;
        }
        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(15); // Why 17? Because it looks good.
        }
        userMarker.setPosition(place.geometry.location);
        updateMarkerPosition(userMarker.getPosition());
        geocodePosition(userMarker.getPosition());
        //geocodePosition(marker.getPosition());
    });
};

function showLocationChoser() {
    $('#getLocationLatlng').modal('show');
    getLocation();
};
window.getLocation = function() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(initialize);
        $('#locationNotAvaliable').hide('400');
    } else {
        $('#locationNotAvaliable').show('400');
        $('#locationNotAvaliable').html('Geolocation is not supported by this browser.');
    }
};

function sendLatLng() {
      $("#locationNotAvaliable").show();
      $('#locationNotAvaliable').html(lat + '  ' + lng);
      console.log(lat + '  ' + lng);
      var data = {'lat':lat, 'lng':lng};
      $.get(URL, data)
};