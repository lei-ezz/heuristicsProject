$(document).ready(function () {
  $("#timer").stopwatch().bind('tick.stopwatch', function (e, elapsed) {
    if (elapsed >= 20001) {
      nextImage(elapsed, 0);
      $(this).stopwatch('reset');
    }
  }).stopwatch('start')
});