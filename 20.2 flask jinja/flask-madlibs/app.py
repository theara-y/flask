from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import json
from madlibs_data import get_madlibs, get_madlib_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    # madlibs = get_madlibs()
    return render_template('home.html', madlibs = get_madlibs())

@app.route('/madlib_form')
def madlib_form():
    madlib_id = int(request.args['madlib_id'])
    madlib = get_madlib_by_id(madlib_id)
    return render_template('madlib_form.html', madlib_id = madlib_id, prompts = madlib.prompts)

@app.route('/show_madlib', methods=["POST"])
def show_madlib():
    madlib_id = int(request.args['madlib_id'])
    madlib = get_madlib_by_id(madlib_id)
    completed_madlib = madlib.generate(request.form)
    return render_template('show_madlib.html', completed_madlib = completed_madlib)