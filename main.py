from serial import Serial
import time

port = "/dev/cu.usbmodem11201"
arduino = Serial(port=port, baudrate=115200, timeout=.1)


while True:
    # num = input("Enter a number: ")  # Taking input from user
    value = arduino.readline()
    print(value.decode("utf-8"))  # printing the value
