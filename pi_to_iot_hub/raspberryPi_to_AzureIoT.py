"""
 Author: Brandon O'Briant
 Date: 11/25/2021
 Description: This program reads in sensor data from Arduino Uno via serial communications and
 sends the data to an Azure IoT Hub through port 443, websockets = True, using symmetric key encryption
 References:
     1: Microsoft Documentation: Connecting to Azure IoT Hub with Symmertric Key and Sending Telemetry Data from Pi to Iot Hub
     2: Python For Undergrad Engineers: Reading Serial Communications from Arduino
"""
# import serial
# import time
# from azure.iot.device import IoTHubDeviceClient, Message
# import json
# import datetime


from main import CONNECTION_STRING


class PiIotConnect:
    """
    Instantiate a connection operation.
    RaspberryPi will attempt connection with Azure IoT Hub by the given Connection String
    and transfer sensor data.

    :param CONNECTION_STRING: the connection string provisioned by Azure IoT Hub
    :type CONNECTION_STRING: str

    :param
    """

    def __init__(self,location, CONECTION_STRING):
        self.location = location
        self.CONNECTION_STRING = CONNECTION_STRING

    def iothub_client_init(self):
        """
        Establish connection to Azure IoT Hub using secure connection string 
        assigned to device in IoT Hub

        :param CONNECTION_STRING: the connection string used for secure connection to Azure IoT Hub
        :type CONNECTION_STRING: string

        """
        client = IoTHubDeviceClient.create_from_connection_string(self.CONNECTION_STRING, websockets=True)
        print("iothub-client-initiated")
        return client


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
                    date_time_str = datetime.datetime.now().isoformat()
                    tmp = str(ser.readline().rstrip(),"utf-8")
                    tmp = tmp.rstrip(tmp[-1])
                    sensor = self.location + tmp[0:8]
                    temp = float(tmp[9::])
                    print(date_time_str + " : " + sensor + " " + str(temp))
                    msg = {"time" : date_time_str, "dspl" : sensor, "temp" : temp}
                    msg = Message(json.dumps(msg))
                    msg.content_encoding = "utf-8"
                    msg.content_type = "application/json"
                    client.send_message(msg)
                    print("Message Successfully sent")
        except KeyboardInterrupt:
            print("IoTHubClient stopped")
