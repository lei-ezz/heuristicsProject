import helper

def getItems():
    # Connect to the databsae 
    con, cur = helper.start()

    # Run the query
    cur.execute(
        'SELECT Item.name, Item.price'
        ' FROM Item;'
    )

    # Get the results
    item_array = cur.fetchall()

    # Terminate the connection
    helper.stop(con, cur)

    # Return the results (Array of Tuples)
    return item_array
