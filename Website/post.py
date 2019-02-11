# For flask, mysql, crypto
from flask import Blueprint, render_template, Response, request
import json
import helper
import datetime

post = Blueprint('post', __name__)

@post.route('/booking', methods=['POST'])
def book():
    data = request.json
