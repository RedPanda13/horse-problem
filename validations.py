def movement_validation_within_board(movement):
    valid_move = True

    if 7 > movement[1][0] < 0:
        valid_move = False
    if 7 > movement[1][1] < 0:
        valid_move = False

    return valid_move


def validation_visited_squares(movement, visited_squares):
    valid_move = True if movement[1] not in visited_squares else False

    return valid_move
