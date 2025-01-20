from sensirion_i2c_driver import I2cConnection
from sensirion_i2c_scd.scd4x import Scd4xI2cDevice

connection = I2cConnection()
sensor = Scd4xI2cDevice(connection)

sensor.start_periodic_measurement()
print("Sensor warming up...")

# Basic Fnctionality for testing - Will convert to class
while True:
    co2, temp, humidity = sensor.read_measurement()
    print(f"CO2: {co2} ppm, Temp: {temp} °C, Humidity: {humidity} %RH")
