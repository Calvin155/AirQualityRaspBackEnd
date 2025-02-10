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
        logging.error(e)

def full_mock():
    # For testing without raspberry pi locally
    try:
        count = 0

        while True:
            random_number_one_pm = random.randint(0, 30)
            random_number_two_pm = random.randint(30, 49)
            random_number_three_pm = random.randint(50, 75)

            co2 = random.randint(15, 20)
            temp = random.randint(9, 12)
            humidity = random.randint(50, 60)
            print("Entered While Loop")

            try:
                influx_db.write_pm_data(random_number_one_pm + count, random_number_two_pm + count, random_number_three_pm + count)
                influx_db.write_co2_temp_hum_data(co2, temp, humidity)
                count = count + 2
                print("Success")
                if count == 10:
                    count = count - 10
                time.sleep(10)
            except Exception as e:
                print(f"Exception in full_mock inner try: {str(e)}")

    except Exception as e:
        print(f"Exception in full_mock outer try: {str(e)}")

# Main Entry Point
while True:
    try:
        time.sleep(30)
        print("Starting")
        pm_sensor.read_data()
        mock_co2_data()
        print("Success")
        time.sleep(15)
    except Exception as e:
        print(f"Exception in main loop: {e}")



