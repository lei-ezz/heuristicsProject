from flask import Response
import mysql.connector
import json

def start (): 
    connect = mysql.connector.connect(
        user = '<username-here>', 
        password = '<password-here>',
        host = '<database-host-here>',
        database = '<database-name-here>', 
        buffered = True
    )
    cursor = connect.cursor()
    return connect, cursor

def stop (con, cursor):
    cursor.close()
    con.close()

def error():
    return Response(json.dumps({'error' : 'an error occured'}), status=404, mimetype='application/json')