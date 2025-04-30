from Sensors.particulate_matter import PM7003Sensor
import time
import logging

# Main Entry
time.sleep(20)
while True:
    try:
        pm_sensor = PM7003Sensor()
        if pm_sensor.is_connected:
            pm_sensor.read_data()
            logging.info("Data Successfully Read and written to Influx DB")
            time.sleep(15)
        else:
            pm_sensor = PM7003Sensor()
    except Exception as e:
        logging.error(f"Exception in main loop: {e}")




