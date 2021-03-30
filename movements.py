from random import randint


def possible_movements(current_position):
    movement_up_right = [current_position[0] - 2, current_position[1] + 1]
    movement_up_left = [current_position[0] - 2, current_position[1] - 1]

    movement_down_right = [current_position[0] + 2, current_position[1] + 1]
    movement_down_left = [current_position[0] + 2, current_position[1] - 1]

    movement_left_up = [current_position[1] - 2, current_position[0] - 1]
    movement_left_down = [current_position[1] - 2, current_position[0] + 1]

    movement_right_up = [current_position[1] + 2, current_position[0] - 1]
    movement_right_down = [current_position[1] + 2, current_position[0] + 1]

    movements = [
                    ['movement_up_right', movement_up_right], ['movement_down_right', movement_down_right],
                    ['movement_right_up', movement_right_up], ['movement_right_down', movement_right_down],
                    ['movement_up_left', movement_up_left], ['movement_down_left', movement_down_left],
                    ['movement_left_up', movement_left_up], ['movement_left_down', movement_left_down],
                ]

    return movements


def get_random_movement(movements):
    chosen_movement = movements[randint(0, 7)]

    return chosen_movement
