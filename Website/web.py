# For flask, mysql, crypto
from flask import current_app, Blueprint, render_template, send_from_directory
import lounger
import os

# Setup the get blueprint
web = Blueprint('web', __name__)

# Returns the root
@web.route('/', methods=['GET'])
def index():
    """Routes '/' to index.html"""
    return render_template('index.html')

# More browser endpoints here
@web.route('/loungers', methods=['GET'])
def loungers():
    #We'll need the number of loungers, etc
    l = (5, ) * lounger.getNumLounger()
    return render_template('lounger.html', loungers=l, number=lounger.getNumLounger())

@web.route('/orders', methods=['GET'])
def orders():
    #We'll need the number of loungers, etc
    return render_template('drink_selection.html')

@web.route('/contacts', methods=['GET'])
def contacts():
    #We'll need the number of loungers, etc
    return render_template('contact.html')

# For downloading files
@web.route('/files/<path:filename>', methods=['GET'])
def download(filename):
    """Download the file"""
    uploads = os.path.join(current_app.root_path,
                           current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)
