$(function(){
  $('button').click(function(){
    var bandName = document.getElementById("mySearch").value;
    document.getElementById("originBand").innerHTML = bandName;
    $.ajax({
      type: 'POST',
      url: '/bandList',
      data: {bandName:bandName},
      success: function(response){
        console.log(response);
        var bandSim = JSON.stringify(response, null, 8); // spacing level = 4
        bandSim = bandSim.replace(/\"/g, "");
        if (response == null){
          var none = "None found";
          document.getElementById("output").innerHTML = none;
          
        }else{
          document.getElementById("output").innerHTML = bandSim;         
        }
        
      },
      error: function(error){
        console.log(error);
        document.getElementById("output").innerHTML = "None found";

      }
    });
  });
});

