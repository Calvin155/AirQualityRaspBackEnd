from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import logging
import os

# Database connections
# Local IP address - Database stored on my laptop
# For Local dev/testing
# Change IP address if want raspberry pi to write to local db db on dev machine
# URL = "http://192.168.1.47:8086"
# TOKEN = "BocuA2JSjjFDITXknBnL9E1X4ADJoNEkJe5IrvNisBSfutGqSOvDZ8EZUccUo76Oc-WBsw-HM2PF9BWGH8VdhQ=="

URL="http://192.168.1.35:8086"
TOKEN="7KoJpNuWfJmldZL5-VhLyHQYk-i97ttvJ29Dep0fJ85yJv89_uB0FabyBXMN7x_-hRV7vvDZHSsRw2PTHW14cg=="
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
                logging.info("Successfully Connected to Influx Database")
                print("Successfully connected to Influx")
            else:
                logging.info("Already connected to Influx Database")
                print("Already connected to Influx")

        except Exception as e:
            logging.error("Error Connecting to Database: " + str(e))



    def write_data(self, measurement, tags, fields):
        try:
            point = {
                "measurement": measurement,
                "tags": tags,
                "fields": fields
            }
            self.write_api.write(bucket=self.bucket, record=point)
            logging.info("Data Written Successfully to Database")
        except Exception as e:
            logging.error("Error Writing Data to Database")

    def write_pm_data(self, pm1, pm2_5, pm10):
        try:
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
            logging.info("Data Written Successfully to Database")
        except Exception as e:
            print("Error writing data to Database" + e)

    def write_co2_temp_hum_data(self, co2, temp, humidity):
        try:
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
            logging.info("CO2, Temp & Humidity Data Written Successfully to Database")
        except Exception as e:
            print("Error writing data to Database - CO2 Sensor" + e)

    def close(self):
        if self.client:
            self.client.close()
            logging.info("Connection to Database Closed")
