if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
}

// This comes from JS global objects and built-in functions.

function showPosition(pos) {
    console.log(pos.coords.latitude, pos.coords.longitude);
}