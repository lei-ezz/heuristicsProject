import helper
import datetime

def getBooked():
    con, cur = helper.start()
    current_dt = datetime.datetime.now()

    # Get Data
    cur.execute(
        'SELECT Lounger.id'
        ' FROM Booking'
        ' INNER JOIN Lounger ON Booking.lounger = Lounger.id'
        ' WHERE Booking.start_time < %s AND Booking.finish_time > %s;',
        (current_dt, current_dt)
    )
    booking_result = cur.fetchall()

    # Close Down
    helper.stop(con, cur)

    # Turn tuple into array
    useful_results = [x for xs in booking_result for x in xs]

    print(useful_results)

    # Return array of integers
    return useful_results

def getLoungerInfo(id):
    con, cur = helper.start() 
    chair_id = id

    cur.execute(
        'SELECT Lounger.name, Lounger.desc'
        ' FROM Lounger'
        ' WHERE Lounger.id = %s'
        ' LIMIT 1;',
        (chair_id, )
    )
    lounger_info = cur.fetchall()

    helper.stop(cur, con)

    return lounger_info[0]

def getNumLounger():
    con, cur = helper.start()

    cur.execute(
        'SELECT COUNT(Lounger.id) '
        'FROM Lounger;'
    )
    numOfLounger = cur.fetchall()

    helper.stop(cur, con)

    numOfLounger = list(numOfLounger[0])

    return numOfLounger[0]

getNumLounger()