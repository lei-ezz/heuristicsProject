# For flask, mysql, crypto
from flask import Blueprint, render_template, Response, request
import lounger
import json
from helper import error

get = Blueprint('get', __name__)

# Expected usage is that when the user clicks on a lounger and it is taken to the lounger_detail page this method will trigger the id
# will be passed into the SQL query
@get.route('/lounger_info', methods=['POST'])
def lounger_info():
    data = request.json

    if data:
        dataDict = json.loads(json.dumps(data))
        if 'id' in dataDict:
            if dataDict['id'] > 0:
                info = lounger.getLoungerInfo(dataDict['id'])
                if info:
                    return Response(json.dumps({'lounger' : {info[0] : info[1]}}), status=200, mimetype='application/json')
                else:
                    return error()
            else:
                return error()
        else:
            return error()
    else:
        return error()