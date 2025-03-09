from flask import Flask, request, make_response, render_template, Response, send_from_directory, jsonify
import pandas as pd
import os
import uuid


app = Flask(__name__, template_folder='templates')


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 

        if username == 'admin' and password == 'admin':
            return 'Login successful'
        else:
            return 'Login failed'

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode('utf-8')
    elif file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']:
        df = pd.read_excel(file)
        return df.to_html()
    else:
        return "Invalid file type"


@app.route('/convert_csv', methods = ['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)

    response = Response(
        df.to_csv(index=False),
        mimetype='text/csv',
        headers={'Content-Disposition' : 'attachment; filename=result.csv' }

    )
    return response


@app.route('/convert_csv_two', methods = ['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))
    return render_template('download.html', filename=filename)


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')


@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json.get('greeting')
    name = request.json.get('name')

    with open('file.txt', 'w') as f:
        f.write(f'{greeting} {name}')

    return jsonify({'message': 'Successfully written'})
            

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
