import os

from flask import Flask
from package import compute

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 4567))

@app.route('/hello')
def hello():
    return f'Hello, World! {compute.return_random()}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
