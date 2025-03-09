from flask import Flask, request, make_response, render_template, Response, send_from_directory, jsonify, session
import pandas as pd
import os
import uuid


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'changelaterkey'

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html', message = 'Index')


@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello world'
    return render_template('index.html', message = 'Session data set.')


@app.route('/get_data')
def get_data():
    if "name" in session.keys() and "other" in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message = f'Name: {name}, other: {other}')
    else:
        return render_template('index.html', message = 'No session data')




if __name__ == '__main__':  
    app.run(host="0.0.0.0", port=5555, debug=True)
