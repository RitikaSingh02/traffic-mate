function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
    var lat = position.coords.latitude;
    var long = position.coords.longitude;
    console.log(lat , long)
    const data = { "lat": lat.toString()  , "long" : long.toString()};
    let response_data;
    fetch('https://traffic-mate.herokuapp.com/maps/location',
      {
        'method':'post',
        'body':JSON.stringify(data)
      }
      ).then(function(res){
        data=>res.json();
      }).then(
        (data) => {
          response_data = data;
        }
      );
        console.log(response_data);
}
function submit(){
  const form = document.getElementsByClassName("form");
  const pick = $('#pick').val();
  const drop = $('#drop').val();
  console.log(pick , drop);
  const data = { "pick": pick  , "drop" : drop};
  location.replace("https://traffic-mate.herokuapp.com/maps/main/" + pick +'/' + drop);
}