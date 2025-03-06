from flask import Flask, request, make_response, render_template




app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    myvalue = "NeuralNine"
    myresauls = 10 + 20
    mylist = [1, 3, 3, 5, 6]

    return render_template('index.html', myvalue=myvalue, myresauls=myresauls, mylist=mylist)

@app.route('/other')
def other():
    some_text = "hello text"
    return render_template('other.html', some_text=some_text)

@app.template_filter('reverse_filter')
def reverse_filter(s):
    return s[::-1]

@app.template_filter('repeat_filter')
def repeat_filter(s, times=2):
    return s * times

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
