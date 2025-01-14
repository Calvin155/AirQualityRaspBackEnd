from AirQualityRasp.Sensors.particulate_matter import PM7003Sensor
import time

pm_sensor = PM7003Sensor

while True:
    # Particulate Matter Sensor
    pm_sensor.read_data()
    time.sleep(15)

# Will need to consider multi threading or a seperate docker container to run both sensors concurrently
# Other sensor CO2, temp & humidity - 3 in 1 sensor - to be added later

