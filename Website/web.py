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


@web.route('/intro', methods=['GET'])
def settings():
    """Routes '/intro' to intro1.html"""
    return render_template('intro1.html')

@web.route('/story', methods=['GET'])
def story():
    """Routes '/story' to intro2.html"""
    return render_template('intro2.html')

# Returns the root
@web.route('/start', methods=['GET'])
def start():
    """Routes '/start' to start.html"""
    return render_template('start.html')
