# .\.venv\Scripts\Activate.ps1

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)
    