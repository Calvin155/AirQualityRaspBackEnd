from Sensors.particulate_matter import PM7003Sensor
import time
import logging

# Main Entry Point
time.sleep(20)
while True:
    try:
        pm_sensor = PM7003Sensor()
        if pm_sensor.is_connected:
            pm_sensor.read_data()
            time.sleep(15)
        else:
            pm_sensor = PM7003Sensor()
    except Exception as e:
        print(f"Exception in main loop: {e}")




