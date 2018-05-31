# helper for sending commands and receiving data from STM32F100 board

import time
import json
import serial
import warnings

class STMBoard:
    def __init__(self, uart="/dev/ttyS1", baudRate=9600):

        try:
            # print "opening serial port"
            self.port = serial.Serial(
			port=uart, 
			baudrate=baudRate,
			parity=serial.PARITY_ODD,
			stopbits=serial.STOPBITS_TWO,
			bytesize=serial.SEVENBITS)
        except x:
            warnings.warn("Can't open the serial port. Please close any applications using the serial port and try again.");
            raise x;
        
    # send a command and request a JSON response
    def getMeasures(self):

        response = ''

	while self.port.inWaiting() > 0:
            response += ser.read(1)

        # response should be encoded in json
        
	try:
            jsonResponse = json.loads(response)
        except x:
            warnings.warn("No response from board")
            return None
        return jsonResponse
