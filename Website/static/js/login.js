// JavaScript Document

$(document).ready(function(){
                  $("#submit").bind("click", validate);
                  });

//Validates a username and password
function validate() {
    var booking = getCookie("booking");
    
    var jsondata;
    if(booking) {
        jsondata = { "user": $("#username").val(), "pass": $("#password").val(), "booking": 0 };
    } else {
        jsondata = { "user": $("#username").val(), "pass": $("#password").val(), "booking": 1 };    
    }

            $.ajax({type: "POST",
                    url: "/post/login",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify(jsondata),
                    success: function(result) {
                        //Store session to check for later and redirect
                        if(!booking){
                            setCookie("booking", result.booking, 7);
                        }
                        setCookie("client", 4 /*TODO: Change this!*/, 7);
                        location.assign(location.protocol + "/loungers");
                    },

                    error: function() {
                        $("#theerror").html("<p style='color: red;'>An error occured! Please try again!</p>");
                    }});
            return false;
}

//Sets a cookie on the document name to value for days daya
function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    } document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

//Get's the cookie with name name
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    } return null;
}