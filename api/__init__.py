from flask import Flask

app = Flask(__name__)

# Initialize Flask extensions here

# Register blueprints here
from .fictionary import bp as fictionary_bp
app.register_blueprint(fictionary_bp, url_prefix='/fictionary')

@app.route('/')
def hello_world():
    return 'Hello, World!'
