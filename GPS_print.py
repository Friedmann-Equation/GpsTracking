# import serial
# import pynmea2

# while True:
#     port = "/dev/ttyAMA0"
#     ser = serial.Serial(port, baudrate=9600, timeout=0.5)
#     dataout = pynmea2.NMEAStreamReader()
#     newdata = ser.readline()
#     n_data = newdata.decode('latin-1')
#     if n_data[0:6] == '$GPRMC':
#         newmsg = pynmea2.parse(n_data)
#         lat = newmsg.latitude
#         lng = newmsg.longitude
#         gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
#         print(gps)
# this is GPS_print.py

import time

while True:
    # Simulated GPS data
    lat = 37.7749  # Replace with desired latitude
    lng = -122.4194  # Replace with desired longitude

    gps = f"Latitude={lat} and Longitude={lng}"
    print(gps)

    time.sleep(1)  # Adjust sleep time as needed
