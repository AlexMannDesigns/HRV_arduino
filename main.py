from serial import Serial
from time import time

MEDITATION_TIME = 180

def meditation_control(arduino: Serial):
    bpm = []
    delta = []
    current_time = time()
    end_time = current_time + MEDITATION_TIME

    while time() < end_time:
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

    return bpm, delta


def control(arduino: Serial):
    # start meditating?

    bpm, delta = meditation_control(arduino)


if __name__ == "__main__":
    port = "/dev/cu.usbmodem11201"
    control(Serial(port=port, baudrate=115200, timeout=.1))
