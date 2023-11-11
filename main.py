from serial import Serial
#import time


def control():
    port = "/dev/cu.usbmodem11201"
    arduino = Serial(port=port, baudrate=115200, timeout=.1)

    #bpm = []
    #delta = []
    while True:
        value = arduino.readline()
        print(value.decode("utf-8"))  # printing the value
        decoded_value = value.decode("utf-8")
        if decoded_value.startswith("BPM"):
            print(decoded_value)
        else:
            print(int(decoded_value))


if __name__ == "__main__":
    control()
