from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import logging
import os

INFLUXDB_URL = os.getenv("INFLUXDB_URL")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
ORG="AQI"
BUCKET="AQIMetrics"


class InfluxDB:
    def __init__(self):
        self.url = INFLUXDB_URL
        self.token = INFLUXDB_TOKEN
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
            else:
                logging.info("Already connected to Influx Database")

        except Exception as e:
            logging.exception("Error Connecting to Database: ", str(e))

    def connected(self):
        try:
            if self.client.ping() == 200:
                logging.info("Connected & Pinging")
                return True
            else:
                logging.info("Not Connected")
                return False
        except Exception as e:
            logging.exception(e)



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
                logging.exception("Error Writing Data to Database")

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
            logging.exception("Error writing data to Database:", str(e))

    def write_co2_temp_hum_data(self, co2, temp, humidity):
        try:
            timestamp = datetime.utcnow().isoformat()
            logging.info(timestamp)
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
            self.write_api.write(bucket=self.bucket, record=point)
            logging.info("Successfully wrote data to Database")
        except Exception as e:
            logging.exception("Error writing data to Database - CO2 Sensor", str(e))

    def close(self):
        if self.client:
            self.client.close()
            logging.info("Connection to Database Closed")
