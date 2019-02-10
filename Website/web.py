# For flask, mysql, crypto
from flask import current_app, Blueprint, render_template, send_from_directory
import os

# Setup the get blueprint
web = Blueprint('web', __name__)

# Returns the root
@web.route('/', methods=['GET'])
def index():
    """Routes '/' to index.html"""
    return render_template('index.html')

# Returns the root
@web.route('/start', methods=['GET'])
def strat():
    """Routes '/start' to start.html"""
    return render_template('start.html')
