# .\.venv\Scripts\Activate.ps1

from flask import Flask, request, make_response




app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route("/hello", methods=['GET'])
def hello():
    response = make_response('Hello obs')
    response.status_code = 202
    response.headers['Content-Type'] = 'application/json'
    return response



@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"


@app.route('/handle_url_params')
def handle_params():

    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting', 'Hello')
        name = request.args.get('name', 'World')
        return f"{greeting}, {name}!"
    else:
        return "No greeting or name provided"




@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"The sum of {number1} and {number2} is {(number1) + (number2)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
