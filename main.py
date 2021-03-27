from random import randint

bord = [
    ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
    ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
    ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
    ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
    ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
    ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
    ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
    ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']
]


def walking(current_position):
    walking_up_right = [current_position[0] + 2, current_position[1] + 1]
    walking_up_left = [current_position[0] + 2, current_position[1] - 1]

    walking_down_right = [current_position[0] - 2, current_position[1] + 1]
    walking_down_left = [current_position[0] - 2, current_position[1] - 1]

    walking_left_up = [current_position[1] - 2, current_position[0] + 1]
    walking_left_down = [current_position[1] - 2, current_position[0] - 1]

    walking_right_up = [current_position[1] + 2, current_position[0] + 1]
    walking_right_down = [current_position[1] + 2, current_position[0] - 1]

    ways = [
            walking_up_right, walking_up_left, walking_down_right, walking_down_left,
            walking_left_up, walking_left_down, walking_right_up, walking_right_down
           ]

    return ways