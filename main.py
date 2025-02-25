from Sensors.particulate_matter import PM7003Sensor
from Database.influxdb import InfluxDB
import time
import random
import logging

pm_sensor = PM7003Sensor()
# Main Entry Point
while True:
    try:
        influx_db = InfluxDB()
        if pm_sensor.is_connected:
            print("Step 1")
            pm_sensor.read_data()
            print("Step Final")
            time.sleep(15)
        else:
            pm_sensor = PM7003Sensor()
    except Exception as e:
        print(f"Exception in main loop: {e}")




