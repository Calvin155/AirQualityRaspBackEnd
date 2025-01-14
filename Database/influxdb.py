from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import logging

URL = "http://localhost:8086"
TOKEN = "uZN6CUu5d5-rLH0eMp21ISKJ0ZU3u3TtYqYshkO0rTx2uxlOl-GAneWoRqUqoYfmZouN0fYOZUaSUq7-7NPMEQ=="
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
            if not self.client:
                self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
            logging.info("Successfully Connected to Influx Database")
        except Exception as e:
            logging.error("Error Connecting to Database" + e)

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

            self.write_api.write(bucket=self.bucket, record=point)
            logging.info("Data Written Successfully to Database")
        except Exception as e:
            logging.error("Error writing data to Database" + e)

    def close(self):
        if self.client:
            self.client.close()
            logging.info("Connection to Database Closed")
