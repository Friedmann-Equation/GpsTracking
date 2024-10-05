import serial
import pynmea2
import pyrebase
import requests

firebaseConfig = {
    "apiKey": "AIzaSyB-sRD6NtNY4-YmzL99uVLjhDmxrTEdZpU",
    "authDomain": "tracking-70c66.firebaseapp.com",
    "projectId": "tracking-70c66",
    "storageBucket": "tracking-70c66.appspot.com",
    "messagingSenderId": "151898302414",
    "appId": "1:151898302414:web:44c029dee4b32eaeeeed9f",
    "measurementId": "G-FWV78JWVX0",
    "databaseURL": "https://tracking-70c66-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

while True:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()

    if newdata[0:6] == b'$GPRMC':
        newmsg = pynmea2.parse(newdata.decode('utf-8'))
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
        print(gps)
        data = {"LAT": lat, "LNG": lng}
        
        try:
            db.update(data)
            print("Data sent")
        except requests.exceptions.JSONDecodeError:
            print('Failed to decode JSON from response')
        except requests.exceptions.RequestException as req_err:
            print(f'Other error occurred: {req_err}')