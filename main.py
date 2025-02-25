from Sensors.particulate_matter import PM7003Sensor
from Database.influxdb import InfluxDB
import time
import random
import logging

while True:
    try:
        influx_db = InfluxDB()
        pm_sensor = PM7003Sensor()

        if influx_db.connected() and pm_sensor.is_connected():
            print("Step 1")
            pm_sensor.read_data()
            print("Step Final")
            time.sleep(15)
        else:
            print("Database or sensor not connected. Retrying in 5 seconds...")
            time.sleep(5)

    except Exception as e:
        print(f"Exception in main loop: {e}")
        time.sleep(5)





