function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
    var lat = position.coords.latitude;
    var long = position.coords.longitude;
    console.log(lat , long)
    const data = { "lat": lat.toString()  , "long" : long.toString()};
    // localStorage.setItem("pick-lat" , lat);
    // localStorage.setItem("pick-long" , long);
    var curr_origin = window.location.origin;
    var url = curr_origin + '/maps/location';
    let response_data;
    fetch(url,
      {
        'method':'post',
        'body':JSON.stringify(data)
      }
      ).then(
        response=>response.json().then(
          data=>(
            {
              data:data.data,
              status:response.status
            }
          )
        ).then(
          res=>{
            response_data = res.data;
            console.log(response_data);             
            document.getElementById("pick").value = response_data['address'];
            // console.log(res.status , res.data);
          }
        )
      )

}
function submit(){
  const pick = $('#pick').val();
  const drop = $('#drop').val();
  var data = {"drop" : pick};
  let response_data;
  var curr_origin = window.location.origin;
  var url = curr_origin + '/maps/get_coordinates'
  fetch(url,
    {
      'method':'post',
      'body':JSON.stringify(data)
    }
    ).then(
      response=>response.json().then(
        data=>(
          {
            data:data.data,
            status:response.status
          }
        )
      ).then(
        res=>{
          response_data = res.data;
          console.log(response_data);       
          localStorage.setItem("pick-lat" , response_data['lat']);
          localStorage.setItem("pick-long" , response_data['long']);
          // console.log(pick , drop);
          // const data = { "pick": pick  , "drop" : drop};
        }
      )
    )
    data = {"drop" : drop};

  fetch(url,
    {
      'method':'post',
      'body':JSON.stringify(data)
    }
    ).then(
      response=>response.json().then(
        data=>(
          {
            data:data.data,
            status:response.status
          }
        )
      ).then(
        res=>{
          response_data = res.data;
          console.log(response_data);       
          localStorage.setItem("drop-lat" , response_data['lat']);
          localStorage.setItem("drop-long" , response_data['long']);
          // console.log(pick , drop);
          // const data = { "pick": pick  , "drop" : drop};
          window.location.href = curr_origin + "/maps/main/" + pick +'/' + drop;      
        }
      )
    )

}