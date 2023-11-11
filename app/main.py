from serial import Serial
from time import time
from math import floor

from print_progress_bar import print_progress_bar
from normalise_list_data import normalise_list_data
from rmssd import get_rmssd_score

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
        print_progress_bar(iteration=((end_time - current_time) / MEDITATION_TIME) * 100)
        current_time = floor(time())
        # test = get_rmssd_score(delta)

    print()  # prints a nl under prog bar
    normalise_list_data(bpm)
    normalise_list_data(delta)
    return bpm, delta


def app_control(arduino: Serial) -> None:
    # start meditating?
    while True:
        response = input("psssst... hey, hey you, hey kid. You wanna start meditating? (yes / no): ")
        if response.lower() in ("y", "yes"):
            bpm, delta = meditation_control(arduino)
            print(f"Average BPM = {sum(bpm) / len(bpm)}")
            print(delta)
        elif response.lower() in ("n", "no"):
            return


if __name__ == "__main__":
    app_control(Serial(port="/dev/cu.usbmodem11201", baudrate=115200, timeout=.1))
