from flask import Flask, render_template
from subprocess import Popen

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gps')
def gps():
    Popen(['python', 'GPS_print.py'])

    Popen(['python', 'GPS_send.py'])

    return render_template('gps.html')

if __name__ == '__main__':
    app.run(debug=True)
