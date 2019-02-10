function startClock(id, endtime){
    var clock = document.getElementById(id);
    var timeinterval = setInterval(function(){
      var t = getTimeRemaining(endtime);
      clock.innerHTML = 'seconds: ' + t.seconds;
      if(t.total<=0){
        clearInterval(timeinterval);
      }
    },1000);
  }

function getTimeRemaining(endtime){
    var t = Date.parse(endtime) - Date.parse(new Date());
    var seconds = Math.floor( (t/1000) % 60 );
    return {
      'total': t,
      'seconds': seconds
    };
  }