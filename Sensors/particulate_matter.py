import serial
import struct
from Database.influxdb import InfluxDB
import logging

class PM7003Sensor:
    def __init__(self, baudrate=9600):
        self.serial_port = '/dev/ttyAMA2'
        self.baudrate = baudrate
        try:
            self.ser = serial.Serial(self.serial_port, self.baudrate, timeout=10)
            logging.info(f"Connected to {self.serial_port} at {self.baudrate} baudrate.")
        except serial.SerialException as e:
            logging.exception(f"Failed to open serial port: {e}")
            raise e 


    def is_connected(self):
        return self.ser is not None and self.ser.is_open
    
    def read_data(self):
        try:
            influx_db = InfluxDB()
            if self.ser.readable():
                data = self.ser.read(32)
                if len(data) > 0 and data[0] == 0x42 and data[1] == 0x4D:
                    pm1_0 = struct.unpack('>H', data[10:12])[0]
                    pm2_5 = struct.unpack('>H', data[12:14])[0]
                    pm10 = struct.unpack('>H', data[14:16])[0]
                    logging.info(f"Particulate Matter 1.0 (PM1.0): {pm1_0} µg/m³")
                    logging.info(f"Particulate Matter 2.5 (PM2.5): {pm2_5} µg/m³")
                    logging.info(f"Particulate Matter 10 (PM10): {pm10} µg/m³")
                    influx_db.write_pm_data(pm1_0,pm2_5,pm10)

            else:
                logging.error("Error Reading Data off PMS7003")

        except Exception as e:
            logging.exception("Error - PM Sensor: " + e)

    def close_connection(self):
        if self.ser.is_open:
            self.ser.close()
            logging.info("Connection Closed")