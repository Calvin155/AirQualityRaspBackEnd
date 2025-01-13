from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

url = "http://192.168.1.191:8086"
token = "uZN6CUu5d5-rLH0eMp21ISKJ0ZU3u3TtYqYshkO0rTx2uxlOl-GAneWoRqUqoYfmZouN0fYOZUaSUq7-7NPMEQ=="
org = "AQI"
bucket = "AQIMetrics"


class InfluxDB:
    def __init__(self):
        self.url = url
        self.token = token
        self.org = org
        self.bucket = bucket
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.query_api = self.client.query_api()

    def connect(self):
        try:
            if not self.client:
                self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
            print("Connected to InfluxDB.")
        except Exception as e:
            print(f"Error connecting to InfluxDB: {e}")

    def write_data(self, measurement, tags, fields):
        try:
            point = {
                "measurement": measurement,
                "tags": tags,
                "fields": fields
            }
            self.write_api.write(bucket=self.bucket, record=point)
            print("Data written successfully.")
        except Exception as e:
            print(f"Error writing data: {e}")

    def write_pm_data(self, pm1, pm2_5, pm10):
        try:
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
            print(f"Data written successfully: {point}")
        except Exception as e:
            print(f"Error writing PM data: {e}")

    def close(self):
        """Close the connection to InfluxDB."""
        if self.client:
            self.client.close()
            print("Connection closed.")
