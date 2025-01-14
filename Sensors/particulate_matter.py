import serial
import struct
from Database.influxdb import InfluxDB

class PM7003Sensor:
    def __init__(self, serial_port='/dev/serial0', baudrate=9600):
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.ser = serial.Serial(self.serial_port, self.baudrate, timeout=2)

    def read_data(self):
        try:
            influx_db = InfluxDB()
            if self.ser.readable():
                data = self.ser.read(32)
                
                if data[0] == 0x42 and data[1] == 0x4D:
                    frame_length = struct.unpack('>H', data[2:4])[0]
                    pm1_0 = struct.unpack('>H', data[10:12])[0]  # PM1.0
                    pm2_5 = struct.unpack('>H', data[12:14])[0]  # PM2.5
                    pm10 = struct.unpack('>H', data[14:16])[0]    # PM10

                    influx_db.write_pm_data(pm1_0,pm2_5,pm10)
                    print(f"Particulate Matter 1.0: {pm1_0}, Particulate Matter 2.5: {pm2_5}, Particulate Matter 10: {pm10}")

            else:
                print("Error")

        except Exception as e:
            print("Error - PM Sensor: " + e)

    def close_connection(self):
        if self.ser.is_open:
            self.ser.close()
            logging.info("Connection Closed")