def movement_validation_within_board(movement):
    valid_move = True if 0 < movement[1][0] < 7 and 0 < movement[1][1] < 7 else False

    return valid_move


def validation_visited_squares(movement, visited_squares):
    valid_move = True if movement[1] not in visited_squares else False

    return valid_move


def valid_move(movement, visited_squares):
    within_board = movement_validation_within_board(movement)
    visited_squares = validation_visited_squares(movement, visited_squares)

    valid_movement = True if within_board and visited_squares else False

    return valid_movement
