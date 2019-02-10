import helper

# Expecting an array of tuples as input parameter
def makeOrder(ids, quantities, booking):
    # Make the connection and cursor
    con, cur = helper.start()

     # Get the size of order table before the new order is added
    cur.execute(
        'SELECT COUNT(Order.id) FROM password.Order;'
    )
    
    number_before = cur.fetchone()
    number_before = number_before[0]

    helper.stop(con, cur)
    con, cur = helper.start()

    for i in range(0, len(ids)):
        query = 'INSERT INTO `Order` (booking, item, quantity) VALUES (%s, %s, %s)'
        cur.execute(query, (booking, ids[i], quantities[i]))
        con.commit()
    
    helper.stop(con, cur)
    con, cur = helper.start()

    # Get the size of order table after the new order is added
    cur.execute(
        'SELECT COUNT(Order.id) FROM password.Order;'
    )

    number_after = cur.fetchone()
    number_after = number_after[0]

    # Check th right number of orders have been added
    did_work = False
    if((number_after - number_before) == len(ids)):
        did_work = True

    print(did_work)

    helper.stop(con, cur)

    return did_work

def addCharge(booking, prices, quantities):
    con, cur = helper.start()

    #find the owner of the booking

    query = 'SELECT `Client`.`id` FROM `Client` INNER JOIN `Booking` ON `Client`.`id` = `Booking`.`client` WHERE `Booking`.`id` = %s'
    cur.execute(query, (booking ,))
    owner = cur.fetchone()[0]

    helper.stop(con, cur)
    
    #add the total of price[i] * quantities[i] to the owner's account
    total_charge = 0

    for i in range(0, len(prices)):
        total_charge = total_charge + (prices[i] * quantities[i])

    con, cur = helper.start()

    query = 'SELECT `spend` FROM `Client` WHERE id = %s'
    cur.execute(query, (owner,))
    current_spend = cur.fetchone()[0]

    helper.stop(con, cur)

    total_charge = total_charge + current_spend

    con, cur = helper.start()

    query = 'UPDATE `Client` SET spend = %s WHERE `Client`.`id` = %s'
    cur.execute(query, (total_charge, owner))
    con.commit()
    helper.stop(con, cur)