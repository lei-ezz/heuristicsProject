# For flask, mysql, crypto
from flask import current_app, Blueprint, render_template, send_from_directory, request, Response
import os, json, csv

# Setup the get blueprint
tocsv = Blueprint('tocv', __name__)

# Returns the root
@tocsv.route('/', methods=['POST'])
def index():
    x = request.json
    result = getLatest() + 1
    f = csv.writer(open("results/results" + str(result) + ".csv", "w"))

    # Write the header
    f.writerow(["Time (s)", "Recommended", "Money ($)"])
    for i in range(1, 21):
        if(i is 1):
            f.writerow([str(x["t" + str(i)] / 1000), x["r" + str(i)], x["money"]])
        else:
            f.writerow([str(x["t" + str(i)] / 1000), x["r" + str(i)], ""])
        i += 1
    return Response(response=json.dumps({ "success" : "success" }), status=200, mimetype='application/json')

def getLatest():
    found = False
    i = 1
    while(found is False):
        try:
            fh = open("results/results" + str(i) + ".csv", "r")
            if(not fh.read()):
                i += 1
            else:
                found = True
            fh.close()
        except:
            return 0
    return i