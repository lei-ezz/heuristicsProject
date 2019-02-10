$(document).ready(function(){
    for (lounger in loungers) {
        $("#book").bind("click", validate(lounger));
    }    
    });

function validate(id) {
    var client = getCookie(client)
    var jsondata;

    if(client) {
        jsondata = { "lounger": id, "start_time": $("#starttime").val(), "finish_time": $("#finishtime").val(), "client": $("#client").val()}
    }

    $.ajax({type: "POST",
                    url: "/post/booking",
                    dataType: "json",
                    contentType: "application/json",
                    data: JSON.stringify(jsondata),
                    success: function(result) {
                        alert("Success!")
                        location.assign(location.protocol + "/loungers");
                    },

                    error: function() {
                        $("#theerror").html("<p style='color: red;'>An error occured! Please try again!</p>");
                    }});
            return false;
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    } return null;
}