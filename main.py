from serial import Serial
from time import time
from math import floor

MEDITATION_TIME = 180


def print_progress_bar(iteration, total=100, prefix='Progress:', suffix='Complete', decimals=1, length=100, fill='█',
                       print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 - (100 * (iteration / float(total))))
    filled_length = 100 - int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)


def meditation_control(arduino: Serial):
    bpm = []
    delta = []
    current_time = time()
    end_time = floor(current_time + MEDITATION_TIME)

    while floor(time()) < end_time:
        value = arduino.readline()
        decoded_value = value.decode("utf-8").rstrip()

        if decoded_value.startswith("BPM"):
            #print(decoded_value)
            bpm.append(float(decoded_value[decoded_value.find('=') + 1:]))
        elif decoded_value:
            #print(decoded_value)
            delta.append(int(decoded_value))
        print_progress_bar(iteration=((end_time - floor(time())) / MEDITATION_TIME) * 100)
        #print(bpm)
        #print(delta)
    print()  # prints a nl under prog bar
    return bpm, delta


def app_control(arduino: Serial):
    # start meditating?
    print("psssst... hey, hey you, hey kid. You wanna start meditating?")

    bpm, delta = meditation_control(arduino)
    print(bpm)
    print(delta)


if __name__ == "__main__":
    app_control(Serial(port="/dev/cu.usbmodem11201", baudrate=115200, timeout=.1))
