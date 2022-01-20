"""
 Author: Brandon O'Briant
 Date: 11/25/2021
 Description: This program reads in sensor data from Arduino Uno via serial communications and
 sends the data to an Azure IoT Hub through port 443, websockets = True, using symmetric key encryption
 References:
     1: Microsoft Documentation: Connecting to Azure IoT Hub with Symmertric Key and Sending Telemetry Data from Pi to Iot Hub
     2: Python For Undergrad Engineers: Reading Serial Communications from Arduino
"""
import serial
import time
from azure.iot.device import IoTHubDeviceClient, Message
import json
import datetime
from raspberryPi_to_AzureIoT import 

web_sockets = True
location = "AK"
CONNECTION_STRING = "<<CHANGE CONNECTION STRING TO ONE PROVIDED FROM AZURE IOT HUB - PRIMARY CONNECTION STRING TO USE SYMMETRIC KEY ENCRYPTION"
ser=serial.Serial("/dev/ttyACM0",9600)
ser.flush()

cnnt = PiIotConnect(location, web_sockets, CONNECTION_STRING)

while True:
    cnnt.pi_iothub_data_transfer(location, CONNECTION STRING):
 
    if __name__ == '__main__':
        print("Press Ctrl-c to stop")
        pi_iothub_data_transfer()