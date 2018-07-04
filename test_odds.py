from flask import Blueprint
from flask import Flask

public = Blueprint('public', __name__, subdomain='odds')


@public.route('/')
def home():
    return 'hello flask'


app = Flask(__name__)
# app.url_map.default_subdomain = 'www'
app.config['SERVER_NAME'] = 'localhost:9000'
app.register_blueprint(public, subdomain='odds')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=9000)
