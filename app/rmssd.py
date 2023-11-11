
import math


def get_rmssd_score(deltas: list) -> float:
    if len(deltas) < 50:
        return 0
    squares = []
    for i in range(len(deltas)):
        squares.append(deltas[i] ** 2)
    mean = sum(squares) / len(squares)
    root = math.sqrt(mean)
    score = math.log(root)
    print(score)
    return score
    # ln 0 - 6.5