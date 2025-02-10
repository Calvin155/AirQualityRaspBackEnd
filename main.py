from Sensors.particulate_matter import PM7003Sensor
from Database.influxdb import InfluxDB
import time
import random
import logging

influx_db = InfluxDB()
pm_sensor = PM7003Sensor()

def mock_co2_data():
    try:
        co2 = random.randint(15,20)
        temp = random.randint(9,12)
        humidity = random.randint(50,60)
        influx_db.write_co2_temp_hum_data(co2, temp, humidity)
    except Exception as e:
        print(e)

# Main Entry Point
while True:
    try:
        print("Starting Pm data")
        pm_sensor.read_data()
        print("Starting mock data")
        mock_co2_data()
        print("Success")
        time.sleep(15)
    except Exception as e:
        print(f"Exception in main loop: {e}")




