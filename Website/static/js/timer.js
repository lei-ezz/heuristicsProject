$(document).ready(
  function startTiming() {
  var a = document.getElementById("timer");
  a = new Stopwatch(a);
  a.start();
})

var Stopwatch = function(elem) {
  var timer       = createTimer(),
      offset,
      clock,
      interval;
 
  // append elements     
  elem.appendChild(timer);
  
  // private functions
  function createTimer() {
    return document.createElement("span");
  }

  function start() {
    if (!interval) {
      offset   = Date.now();
      interval = setInterval(update, 1);
    }
  }

  function update() {
    clock += delta();
    render();
  }
  
  function render() {
    timer.innerHTML = clock / 1000; 
  }
  
  function delta() {
    var now = Date.now(),
        d   = now - offset;
    
    offset = now;
    return d;
  }
  
  // public API
  this.start  = start;
};
