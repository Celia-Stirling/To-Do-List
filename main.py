from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#app = Flask('app')

#@app.route('/')
#def hello_world():
#  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)