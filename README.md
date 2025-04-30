# AirQualityRasp
Author: Calvin Lynch - K00271788
Project - Air Quality Metrics Using A Raspberry Pi 5
Language - Python
Raspberry PI 5 - Air Quality Metrics

Application for PMS7003 Particulate Matter Sensor
Database: Influx Database

Database Requirements: Ensure that you have a database set up & running live. This applciation uses influx database so a URL & an access token with write privelages is required. 
This will require some configuration: Locate the Database folder & then locate influxdb.py.
Locate the following: 

(Alternative to the below if cannot be passed via env variables, remove os.getenv() and pass ip address or tokens in directly)

INFLUXDB_URL = os.getenv("INFLUXDB_URL")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")

These variables will require valid values or the data will now be written - Either update the variable with the database URL:PORT & Token(Not recomended to put these values directly into the source code) or save these as enviromental variables on the system or in a keystore to add an additional layer of security for these variables as they are considerd sensitive.

Raspberry Pi Requirements: Raspberry Pi & PMS7003 sensor(Sensor connected to Raspberry Pi 5 on Serial1(UART Enabled)), Network access, Docker CLI
Packages: Installed in docker container using Poetry Pytomel file

Where to Run this Application: On the Rasoberry as it interacts with the PMS7003 sensor

How to Run: 

Ensure you have this source code on your Raspberry Pi. Whilst connected to your Raspberry Pi(Either Remotely or Directly Plugged in),
Clone this repository onto your Raspberry Pi.

Ensure you have docker installed on your Raspberry Pi as it is needed to create a docker image of the applciation & to run the image in a docker container.

Step 1. Navigate to the root of the project. /AIRQUALITYRASPBACKEND
step 2. Type: "sudo docker build -t 'name_your_image:_v_major_minor_patch' ." 
Note on step 2 -> Name your image & version it using 1.0.1(for versioning) & dont forget the dot at the of the command as this is required in the build command.

step 3. After successfully creating the image, run the Image in a docker container. (To See if the image has been created type: 'sudo docker images')
To run the image type: "sudo docker run -d --device=/dev/serial'num' --privileged -it "image:version"

Please take note of --device=/dev/serial'num' - num is the serial port you which to communicate with the sensor over UART
if the sensor is operating on any other serial port other than 1 please change it in the particulate_matter.py class so the applciation can run successfully & connect to it.

The above command will run the image in a docker conatiner - Since the image was built using poetry as a package manager there is no need to install any aditional dependecies to run this.

What is happening:
    sudo docker -> sudo is super user privelages(can be changed) calling docker to access functionality.
    run -> telling docker to run an image in a docker conatiner - Docker will take an image & run it on a isolated docker container.
    -d -> detatch - detatch the container from the main shell & run it is a seperate background task.

This should now successfully be running the application in a docker container.

If the database is set up correct & You have correctly connected your sensor to the Raspberry Pi - Particulate Matter data will be written & stored in your influx database.

Note: To get an influx database image, visit docker hub https://hub.docker.com/_/influxdb - This page also provides documentation on how to pull, run & access.

If creating a new influx db instance make sure to take note of the following:

Update the influx db class in this applciation:

INFLUXDB_URL = os.getenv("INFLUXDB_URL") - Mentioned above
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN") - Mentioned above
ORG="AQI" - When creating an ORG on the influx UI - type AQI or if changed, change in the influx db class
BUCKET="AQIMetrics" - When creating a Bucket on the influx UI - type AQIMetrics or if changed, change in the influx db class







