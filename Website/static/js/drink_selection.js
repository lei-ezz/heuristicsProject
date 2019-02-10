function createOrder() {
    //get Pauls help with getting all the ordered elements in one go
    //for each loop to iterate through the table rows
    //if the row's quantity element is not 0
    //then add item to order
    //else ignore item

    var menu = document.getElementById("items")
    for (let i = 0; i < table.rows[i]; i++) {
        //check the #quantity for equalling 0
        if(table.rows[i].getElementById("quantity").val() != 0) {
            //add the name and quantity of the item to a string

        }
    }

    var jsondata = { "order": 
        array.forEach(element => {
            {"name:" + $("#name").val(), "quantity:" + $("#quantity").val()}}
        , "booking:" + $(/*booking number*/))};

    $.ajax({type:"POST",
            url: "/post/order",
            dataType: "json",
            contentType: "application/json",
            success: function(result) {
                alert("Successfully ordered!");
            },
            error: function() {
                alert("There was problem with your order, please contact the wait staff");
            }});
}