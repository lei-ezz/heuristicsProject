from flask import Response
import json

def error():
    return Response(json.dumps({'error' : 'an error occured'}), status=404, mimetype='application/json')