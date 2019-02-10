# For flask
from flask import Flask, render_template

# Setup nocache
nocache = True

# Start up the app, disable caching for now
app = Flask(__name__)
if nocache:
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Set the uploads folder so the client can download things
app.config['UPLOAD_FOLDER'] = "uploads"
with app.app_context():
    from web import web
    from get import get
    from post import post

    app.register_blueprint(web)
    app.register_blueprint(get, url_prefix='/get')
    app.register_blueprint(post, url_prefix='/post')

@app.errorhandler(404)
def page_not_found(e):
    """Error handling page"""
    return render_template('404.html'), 404

# Finally, start the server!
if __name__ == '__main__':
    app.run()
