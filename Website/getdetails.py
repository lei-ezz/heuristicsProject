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
