// Checks if you have a valid cookie for session and will display links to either login or to your profile page
$(document).ready(function() {
    setCookie("stage", 1, 3);
    shuffleImages();

    $("#1").bind('click', function() { nextImage(1) });
    $("#2").bind('click', function() { nextImage(2) });
    $("#3").bind('click', function() { nextImage(3) });
    $("#4").bind('click', function() { nextImage(4) });
});

// Updates all of the images
function nextImage(id) {
    if(getCookie("stage") <= 20) {
        storeStage(id);
        shuffleImages();
        recommened();
    } else showButton();
}

function shuffleImages() {
    // Shuffle the images of the next stage
    var images = [1, 2, 3, 4];
    images = shuffle(images);

    $("#1").attr('src', "../static/img/" + getCookie("stage") + "/" + images[0] + ".jpg");
    $("#1").attr
    $("#2").attr('src', "../static/img/" + getCookie("stage") + "/" + images[1] + ".jpg");
    $("#2").attr
    $("#3").attr('src', "../static/img/" + getCookie("stage") + "/" + images[2] + ".jpg");
    $("#3").attr
    $("#4").attr('src', "../static/img/" + getCookie("stage") + "/" + images[3] + ".jpg");
    $("#4").attr
}

function recommened() {
    if(getCookie("stage") > 4) {
        // Add recommened on one of them
        var images = [1, 2, 3, 4];
        images = shuffle(images);

        $("#cool" + images[0]).html("Cool!");
        $("#cool" + images[1]).html("");
        $("#cool" + images[2]).html("");
        $("#cool" + images[3]).html("");
    }
}

function storeStage(id) {
    var stage = getCookie("stage");
    setCookie("stage", parseInt(stage) + 1, 3);

    if()
}

function showButton() {
    // Show the button to export the final results


    // Send AJAX Request to server
}

// https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
  
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
  
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
  
      // And swap it with the current element.
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
  
    return array;
  }

//Get's the cookie with name *name*
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    } return null;
}

//Sets a cookie on the document *name* to *value* for *days* daya
function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    } document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}