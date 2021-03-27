def movement_validation_within_board(movement):
    valid_move = True

    if movement[0] < 0 or movement[0] > 7:
        valid_move = False

    if movement[1] < 0 or movement[1] > 7:
        valid_move = False

    return valid_move


def validation_visited_squares(movement, visited_squares):
    valid_move = True if movement not in visited_squares else False

    return valid_move