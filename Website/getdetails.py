# For flask, mysql, crypto
from flask import current_app, Blueprint, render_template, send_from_directory, request, Response
import os, json, csv

# Setup the get blueprint
gd = Blueprint('gd', __name__)

# Returns the root
@gd.route('/', methods=['POST'])
def make():
    x = request.json

    current_app.participent = x["par"];
    current_app.trail = x["trail"];
    current_app.time = x["time"];
    return Response(response=json.dumps({ "success" : "success" }), status=200, mimetype='application/json')

# Gets the information from the server
@gd.route('/getTime', methods=['POST'])
def get():
    part = current_app.participent
    trail = current_app.trail
    time = current_app.time
    if (part is not None and trail is not None and time is not None):
        return Response(response=json.dumps({ "time" : time }), status=200, mimetype='application/json')
    else:
        return Response(response=json.dumps({ "error" : "error" }), status=500, mimetype='application/json')