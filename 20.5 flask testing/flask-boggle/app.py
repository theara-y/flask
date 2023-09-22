from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route("/")
def render_board():
    session['board'] = boggle_game.make_board()
    return render_template('app.html', board = session['board'])

@app.route("/submit_word")
def submit_word():
    return jsonify({'result': boggle_game.check_valid_word(session['board'], request.args['word'])})

@app.route("/submit_best_score")
def submit_best_score():
    submitted_score = int(request.args['best_score'])
    if session.get('best_score') == None or submitted_score > session['best_score']:
        session['best_score'] = submitted_score
    return jsonify({
        'result': session['best_score']
    })