from flask import Flask, request
import operations

app = Flask(__name__)

math_operations = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div,
}

@app.route('/math/<operation>')
def math(operation):
    a = float(request.args['a']) # request args are strings
    b = float(request.args['b']) # convert str to float

    return str(math_operations[operation](a, b)) #routes can only return string