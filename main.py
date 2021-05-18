from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

todos = ["Learn Flask", "Clean Bathroom", "Organize toys"]

class TodoForm(FlaskForm):
  todo = StringField("To Do")
  submit = SubmitField("Add Todo")

@app.route('/', methods = ["GET", "POST"])
def index():
  if 'todo' in request.form:
    todos.append(request.form['todo'])
  return render_template('index.html', todos=todos, template_form = TodoForm())

app.run(host='0.0.0.0', port=8080)