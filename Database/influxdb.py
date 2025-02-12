from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import logging
import os

# Database connections
URL = "http://54.78.60.93:8086"
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
            print("Error Connecting to Database: " + str(e))

    def connected(self):
        try:
            if self.client.ping():
                print("Connected & Pinging")
            else:
                print("No Joy")
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
            if self.connected():
                timestamp = datetime.utcnow().isoformat()
                point = {
                    "measurement": "air_quality",
                    "tags": {"location": "local"},
                    "fields": {
                        "PM1": round(pm1,2),
                        "PM2.5": round(pm2_5,2),
                        "PM10": round(pm10,2)
                    },
                    "time": timestamp
                }
                self.write_api.write(bucket=self.bucket, record=point)
                print("Data Written Successfully to Database")
            else:
                print("Cant Connect")
        except Exception as e:
            print("Error writing data to Database" + e)

    def write_co2_temp_hum_data(self, co2, temp, humidity):
        try:
            if self.connected():
                timestamp = datetime.utcnow().isoformat()
                point = {
                    "measurement": "air_quality",
                    "tags": {"location": "local"},
                    "fields": {
                        "CO2": round(co2,2),
                        "Temperature": round(temp,2),
                        "Humidity": round(humidity,2)
                    },
                    "time": timestamp
                }
                self.write_api.write(bucket=self.bucket, record=point)
                print("CO2, Temp & Humidity Data Written Successfully to Database")
            else:
                print("Cant Connect")
        except Exception as e:
            print("Error writing data to Database - CO2 Sensor" + e)

    def close(self):
        if self.client:
            self.client.close()
            print("Connection to Database Closed")
