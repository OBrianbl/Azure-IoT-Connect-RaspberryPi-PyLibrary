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


# from tempfile import tempdir
# from main import CONNECTION_STRING


class PiIotConnect:
    """
    Instantiate a connection operation.
    RaspberryPi will attempt connection with Azure IoT Hub by the given Connection String
    and transfer sensor data.

    :param location: Is the location description for sensors (i.e. "AK" for Alaska)
    :type location: str

    :param web_sockets: Establishes the type of connection (i.e. use websockets), takes on two values True, False.
    :type web_sockets: boolean

    :param CONNECTION_STRING: the connection string provisioned by Azure IoT Hub
    :type CONNECTION_STRING: str
    """

    def __init__(self,location, web_sockets, CONECTION_STRING):
        self.location = location
        self.web_sockets = web_sockets
        self.CONNECTION_STRING = CONNECTION_STRING

    def iothub_client_init(self):
        """
        Establish connection to Azure IoT Hub using secure connection string 
        assigned to device in IoT Hub

        :param CONNECTION_STRING: the connection string used for secure connection to Azure IoT Hub
        :type CONNECTION_STRING: string

        """
        client = IoTHubDeviceClient.create_from_connection_string(self.CONNECTION_STRING, websockets=web_sockets)
        print("iothub-client-initiated")
        return client

    def read_arduino_data(self):
        """
        Read data in from Arduino, extract and return pertinent information sensor #, temperature,
        and time stamp of data ingestion.
        
        """
        self.date_time_str = datetime.datetime.now().isoformat()
        tmp = str(ser.readline().rstrip(),"utf-8")
        tmp = tmp.rstrip(tmp[-1])
        self.sensor = self.location + tmp[0:8]
        self.temp = float(tmp[9::])
        return self.date_time_str, self.sensor, self.temp

    def structure_payload(self, time, dspl, temp):
        """
        Structure the message in JSON to send to Azure IoT Hub.

        param: msg: dictionary of time stamp, dspl (i.e. sensor type -- 1,2,3,etc), and temperature 
                    from sensor restructured as JSON
        type: msg: JSON 

        """
        self.date_time_str, self.sensor, self.temp = read_arduino_data()
        msg = {"time" : time, "dspl" : dspl, "temp" : temp}
        msg = Message(json.dumps(msg))
        msg.content_encoding = "utf-8"
        msg.content_type = "application/json"
        return msg

    def pi_iothub_data_transfer(self):
        """
        Connect to Azure IoT Hub and send sensor data from Raspberry Pi to IoT Hub. 

        """
        print("telemetry function started")                                                                                                                                                                                                                                                               
        try:
            client = iothub_client_init()
            print("sending data to IoT Hub, plress Ctrl-c to exit")
            while True:
                if ser.in_waiting > 0:
                    self.date_time_str, self.sensor, self.temp= read_arduino_data()
                    payload = structure_payload(self.time, self.dspl, self.temp)
                    client.send_message(msg)
                    print("Message Successfully sent")
        except KeyboardInterrupt:
            print("IoTHubClient stopped")
