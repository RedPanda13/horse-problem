from random import choice


def possible_movements(current_position):
    movement_up_right = [current_position[0] - 2, current_position[1] + 1]
    movement_up_left = [current_position[0] - 2, current_position[1] - 1]

    movement_down_right = [current_position[0] + 2, current_position[1] + 1]
    movement_down_left = [current_position[0] + 2, current_position[1] - 1]

    movement_left_up = [current_position[0] - 1, current_position[1] - 2]
    movement_left_down = [current_position[0] + 1, current_position[1] - 2]

    movement_right_up = [current_position[0] - 1, current_position[1] + 2]
    movement_right_down = [current_position[0] + 1, current_position[1] + 2]

    movements = [
                    movement_up_right, movement_down_right, movement_right_up, movement_right_down,
                    movement_up_left, movement_down_left, movement_left_up,  movement_left_down
                ]

    return movements


def get_random_movement(movements):
    chosen_movement = movements.pop(movements.index(choice(movements)))

    return chosen_movement
