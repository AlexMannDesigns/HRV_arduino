from serial import Serial

#import time


def control(arduino: Serial):
    bpm = []
    delta = []

    while True:
        value = arduino.readline()
        decoded_value = value.decode("utf-8").rstrip()

        if decoded_value.startswith("BPM"):
            print(decoded_value)
            bpm.append(float(decoded_value[decoded_value.find('=') + 1:]))
        elif decoded_value:
            print(decoded_value)
            delta.append(int(decoded_value))

        print(bpm)
        print(delta)


if __name__ == "__main__":
    port = "/dev/cu.usbmodem11201"
    control(Serial(port=port, baudrate=115200, timeout=.1))
