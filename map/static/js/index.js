window.onload = ()=>{
  var fastest_lat = localStorage.getItem("drop-lat");
  var fastest_long = localStorage.getItem("drop-long");
  var second_lat = (+(fastest_lat) +  +(localStorage.getItem("pick-lat")))/2;
  var second_long = (+(fastest_lat) +  +(localStorage.getItem("pick-lang")))/2;
  let data = {"lat" : fastest_lat , "long" : fastest_long};
  var curr_origin = window.location.origin;
  var url = curr_origin + '/maps/get_weather';
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
          document.getElementsByClassName("temp-first").innerHTML = res.data['temp_in_celcius'];
          document.getElementsByClassName("desc-first").innerHTML = res.data['weather_desc'];
          document.getElementById("weather-first").src = res.data['icon']
          console.log(res.status , res.data);
        }
      )
    );
    data = {"lat" : second_lat , "long" : second_long};
    // console.log(window.location.origin);
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
          document.getElementsByClassName("temp-second").innerHTML = res.data['temp_in_celcius'];
          document.getElementsByClassName("desc-second").innerHTML = res.data['weather_desc'];
          document.getElementById("weather-second").src = res.data['icon']

          console.log(res.status , res.data);
        }
      )
    )


}