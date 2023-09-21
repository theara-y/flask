from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route("/")
def test():
    session['board'] = boggle_game.make_board()
    return render_template('app.html', board = session['board'])

@app.route("/submit_word")
def submit_word():
    return jsonify({'result': boggle_game.check_valid_word(session['board'], request.args['word'])})