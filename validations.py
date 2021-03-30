def movement_within_board(movement):
    within_board = True if 0 < movement[1][0] < 7 and 0 < movement[1][1] < 7 else False

    return within_board


def visited_squares(movement, visited_squares):
    not_visited_squares = True if movement[1] not in visited_squares else False

    return not_visited_squares


def valid_move(movement, visited_squares):
    within_board = movement_within_board(movement)
    not_visited_squares = visited_squares(movement, visited_squares)

    valid_movement = True if within_board and not_visited_squares else False

    return valid_movement
