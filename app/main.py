from serial import Serial
from time import time
from math import floor

from print_progress_bar import print_progress_bar
from normalise_list_data import normalise_list_data
from rmssd import get_rmssd_score
from blob import BLOB

MEDITATION_TIME = 180


def meditation_control(arduino: Serial) -> tuple[list, list]:
    bpm = []
    delta = []
    current_time = time()
    end_time = floor(current_time + MEDITATION_TIME)

    while current_time < end_time:
        value = arduino.readline()
        decoded_value = value.decode("utf-8").rstrip()

        if decoded_value.startswith("BPM"):
            bpm.append(float(decoded_value[decoded_value.find('=') + 1:]))
        elif decoded_value:
            delta.append(int(decoded_value))
        current_time = floor(time())
        print_progress_bar(iteration=((end_time - current_time) / MEDITATION_TIME) * 100)
        # test = get_rmssd_score(delta)
    #print_progress_bar(100)

    print()  # prints a nl under prog bar
    normalise_list_data(bpm)
    normalise_list_data(delta)
    return bpm, delta


def app_control(arduino: Serial) -> None:
    # start meditating?
    while True:
        print(BLOB)
        response = input("Would you like to start meditating? (yes / no): ")
        if response.lower() in ("y", "yes"):
            bpm, delta = meditation_control(arduino)
            if len(bpm):
                print(f"Average BPM = {floor(sum(bpm) / len(bpm))}")
            print(delta)
        elif response.lower() in ("n", "no"):
            print("Goodbye!")
            return


if __name__ == "__main__":
    app_control(Serial(port="/dev/cu.usbmodem11201", baudrate=115200, timeout=.1))
