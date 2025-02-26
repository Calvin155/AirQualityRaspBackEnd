from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import logging
import os

# Database connections
URL = "http://52.212.232.158:8086"
TOKEN="BuCaDsBU6ZVF_stT2gxyyQ_in6h5gBhPpeukPMeF4tHrGD4tCPhldQE2fhm709RAtmbaxOb7eINqWxqyRosDPg=="
ORG="AQI"
BUCKET="AQIMetrics"


class InfluxDB:
    def __init__(self):
        self.url = URL
        self.token = TOKEN
        self.org = ORG
        self.bucket = BUCKET
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()

    def connect(self):
        try:
            if self.client:
                self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
                print("Successfully Connected to Influx Database")
                print("Successfully connected to Influx")
            else:
                print("Already connected to Influx Database")
                print("Already connected to Influx")

        except Exception as e:
            print("Error Connecting to Database: ", str(e))

    def connected(self):
        try:
            if self.client.ping() == 200:
                print("Connected & Pinging")
                return True
            else:
                print("No Joy")
                return False
        except Exception as e:
            print(e)



    def write_data(self, measurement, tags, fields):
            try:
                point = {
                    "measurement": measurement,
                    "tags": tags,
                    "fields": fields
                }
                self.write_api.write(bucket=self.bucket, record=point)
                print("Data Written Successfully to Database")
            except Exception as e:
                print("Error Writing Data to Database")

    def write_pm_data(self, pm1, pm2_5, pm10):
        try:
            pm1 = float(pm1)
            pm2_5 = float(pm2_5)
            pm10 = float(pm10)

            timestamp = datetime.utcnow().isoformat()
            point = {
                "measurement": "air_quality",
                "tags": {"location": "local"},
                "fields": {
                    "PM1": pm1,
                    "PM2.5": pm2_5,
                    "PM10": pm10
                },
                "time": timestamp
            }

            self.write_api.write(bucket=self.bucket, record=point)
        except Exception as e:
            print("Error writing data to Database:", str(e))

    def write_co2_temp_hum_data(self, co2, temp, humidity):
        try:
            print("Step 4 - connected to db - co2")
            timestamp = datetime.utcnow().isoformat()
            print("Step 5 - time stamp")
            print(timestamp)
            point = {
                "measurement": "air_quality",
                "tags": {"location": "local"},
                "fields": {
                    "CO2": co2,
                    "Temperature": temp,
                    "Humidity": humidity
                },
                "time": timestamp
            }
            print("Step 6 - Just aboput to write CO2")
            self.write_api.write(bucket=self.bucket, record=point)
            print(" step 7 CO2, Temp & Humidity Data Written Successfully to Database")
        except Exception as e:
            print("Error writing data to Database - CO2 Sensor", str(e))

    def close(self):
        if self.client:
            self.client.close()
            print("Connection to Database Closed")
