import serial
import struct
from Database.influxdb import InfluxDB
import logging

class PM7003Sensor:
    def __init__(self, baudrate=9600):
        self.serial_port = '/dev/ttyAMA0'
        self.baudrate = baudrate
        try:
            self.ser = serial.Serial(self.serial_port, self.baudrate, timeout=10)
            print(f"Connected to {self.serial_port} at {self.baudrate} baudrate.")
        except serial.SerialException as e:
            print(e)

    def is_connected(self):
        return self.ser is not None and self.ser.is_open
    
    def read_data(self):
        try:
            print("Connecting To DB")
            influx_db = InfluxDB()
            print("Writing To DB 2")
            if self.ser.readable():
                data = self.ser.read(32)
                if data[0] == 0x42 and data[1] == 0x4D:
                    pm1_0 = struct.unpack('>H', data[10:12])[0]
                    pm2_5 = struct.unpack('>H', data[12:14])[0]
                    pm10 = struct.unpack('>H', data[14:16])[0]
                    print("Writing To DB")
                    influx_db.write_pm_data(pm1_0,pm2_5,pm10)

            else:
                print("Error Reading Data off PMS7003")

        except Exception as e:
            print("Error - PM Sensor: " + e)

    def close_connection(self):
        if self.ser.is_open:
            self.ser.close()
            print("Connection Closed")