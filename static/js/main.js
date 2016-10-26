// This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

//  This function creates an <iframe> (and YouTube player)
//  after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '390',
    width: '640',
    videoId: 'M7lc1UVf-VE',
    events: {
      'onReady': onPlayerReady,
    }
  });
}

//  The API will call this function when the video player is ready.
function onPlayerReady(event) {
  event.target.playVideo();
}
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


