# GPS_send.py
import pyrebase
import serial
import pynmea2

firebaseConfig = {
    "apiKey": "AIzaSyBir3g8dAX2aAZU-5f7JGkIz7borPzBKsI",
    "authDomain": "gpstracker-d3103.firebaseapp.com",
    "projectId": "gpstracker-d3103",
    "storageBucket": "gpstracker-d3103.appspot.com",
    "messagingSenderId": "68411226374",
    "appId": "1:68411226374:web:71f244fa987b4bb92b0687",
    "measurementId": "G-SS3ECM88Q2",
    "databaseURL": "https://gpstracker-d3103-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

while True:
    port = "COM4"  # Replace "x" with the correct COM port number, e.g., "COM3"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()
    n_data = newdata.decode('latin-1')
    
    if n_data[0:6] == '$GPRMC':
        newmsg = pynmea2.parse(n_data)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
        print(gps)
        
        data = {"LAT": lat, "LNG": lng}
        db.update(data)
        print("Data sent")
