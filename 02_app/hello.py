from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    PASSWORD = os.environ.get('PASSWORD')
    return 'Hello, World! This is my password -> '+PASSWORD

