# 
# Vienkārša Flask programma HTTP
# Palaid ar: "python3 -m flask --app hello_flask run"
# Atvēr ar: http://127.0.0.1:5000
#
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/projects')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'