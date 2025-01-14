from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import logging

# Database connections

# Local IP address - Database stored on my laptop
URL = "http://192.168.1.191:8086"
TOKEN = "BocuA2JSjjFDITXknBnL9E1X4ADJoNEkJe5IrvNisBSfutGqSOvDZ8EZUccUo76Oc-WBsw-HM2PF9BWGH8VdhQ=="
ORG = "AQI"
BUCKET = "AQIMetrics"


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
            if self.client:  # Only create a new client if self.client doesn't exist
                self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
                logging.info("Successfully Connected to Influx Database")
                print("Successfully connected to Influx")  # Optional, if you need console feedback
            else:
                logging.info("Already connected to Influx Database")
                print("Already connected to Influx")  # Optional feedback for the user

        except Exception as e:
            logging.error("Error Connecting to Database: " + str(e))  # Ensure exception is stringified
            print(f"Error Connecting to Database: {e}")  # Optional console feedback for debugging


    # Example function on how to write to DB
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
            # Iso time format for writing to influx
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
            print("Data about to be written" + str(pm1))
            self.write_api.write(bucket=self.bucket, record=point)
            print("Data Written")
            logging.info("Data Written Successfully to Database")
        except Exception as e:
            print("Error writing data to Database" + e)

    def close(self):
        if self.client:
            self.client.close()
            logging.info("Connection to Database Closed")
