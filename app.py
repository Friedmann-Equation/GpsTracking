from flask import Flask, render_template
from subprocess import Popen
import serial
import pynmea2

app = Flask(__name__, static_url_path='/static')

# Create a dictionary to store GPS data
gps_data = {"latitude": 0.0, "longitude": 0.0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gps')
def gps():
    # Fetch GPS data using your GPS_read.py logic
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()
    n_data = newdata.decode('latin-1')
    
    if n_data[0:6] == '$GPRMC':
        newmsg = pynmea2.parse(n_data)
        gps_data["latitude"] = newmsg.latitude
        gps_data["longitude"] = newmsg.longitude

    gps_data = {"latitude": 123.456, "longitude": -789.012}  # Replace with actual data from Firebase
    return render_template('gps.html', gps_data=gps_data)

if __name__ == '__main__':
    app.run(debug=True)
