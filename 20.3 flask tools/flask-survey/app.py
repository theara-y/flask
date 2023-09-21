from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debugger = DebugToolbarExtension(app)

@app.route("/")
def start_page():
    return render_template(
        'start_survey.html',
        title = satisfaction_survey.title,
        instructions = satisfaction_survey.instructions
    )

@app.route("/post_session", methods=["POST"])
def create_session():
    session["responses"] = []
    return redirect("/questions/0")

@app.route("/questions/<int:questionId>")
def get_question(questionId):
    if len(session["responses"]) == len(satisfaction_survey.questions):
        return redirect("/thank_user")

    if questionId != len(session["responses"]):
        flash("Redirected to current question.")
        return redirect(f"/questions/{len(session['responses'])}")


    question = satisfaction_survey.questions[questionId]
    return render_template(
        'question.html',
        question = question.question,
        choices = question.choices,
        allow_text = question.allow_text
    )

@app.route("/answer", methods=["POST"])
def post_answer():
    answer = request.form['answer']
    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses
    return redirect(f"/questions/{len(session['responses'])}")

@app.route("/thank_user")
def thanks():
    if len(session["responses"]) != len(satisfaction_survey.questions):
        return redirect(f"/questions/{len(session['responses'])}")

    return render_template(
        "thank_user.html"
    )