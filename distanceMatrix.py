import pandas as pd
import math
pattern = input("Enter a pattern: ")


def find_coordinates(matrix, target_value):
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == target_value:
                return row_index, col_index
    return None


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def eucliDist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def move_horizontally(x1, x2):
    return abs(x1 - x2)


def move_vertically(y1, y2):
    return abs(y1 - y2)


def distance(x1, y1, x2, y2):
    if x1 == x2:
        return move_vertically(y1, y2)
    elif y1 == y2:
        return move_horizontally(x1, x2)
    else:
        horizontal_distance = move_horizontally(x1, x2)
        vertical_distance = move_vertically(y1, y2)
        return eucliDist(0, 0, horizontal_distance, vertical_distance)


pairs = []
for i in range(len(pattern) - 1):
    pairs.append((int(pattern[i]), int(pattern[i + 1])))
print("Check pairs here", pairs)
totalDistance = 0
for pair in pairs:
    x1, y1 = find_coordinates(matrix, pair[0])
    x2, y2 = find_coordinates(matrix, pair[1])
    totalDistance += distance(x1, y1, x2, y2)
    print("Distance from", pair[0], "to",
          pair[1], "is", distance(x1, y1, x2, y2))

print("Total distance:", totalDistance, "CM")
