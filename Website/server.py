# For flask
from flask import Flask, render_template

# Setup nocache
nocache = True
global participent
global trial
global time
# Start up the app, disable caching for now
app = Flask(__name__)
if nocache:
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Set the uploads folder so the client can download things
app.config['UPLOAD_FOLDER'] = "uploads"
with app.app_context():
    from web import web
    from convertcsv import tocsv
    from getdetails import gd

    app.register_blueprint(web)
    app.register_blueprint(tocsv, url_prefix='/tocsv')
    app.register_blueprint(gd, url_prefix='/getData')
# Finally, start the server!
if __name__ == '__main__':
    app.run()
