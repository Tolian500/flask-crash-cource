from flask import Flask, request, make_response, render_template, Response, send_from_directory, jsonify, session, flash

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

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message = 'Session cleared')


@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message = 'Cookie set'))
    response.set_cookie('cookie_name', 'cookie_values')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message = f'Cookie value: {cookie_value}')


@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message = 'Cookie removed'))
    response.set_cookie('cookie_name', expires=0)
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
    
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            flash('Sucessfull login!')
            return render_template('index.html', message = '')
        else: 
            flash('Login failed!')
            return render_template('index.html', message = '')
        
        
if __name__ == '__main__':  
    app.run(host="0.0.0.0", port=5555, debug=True)
