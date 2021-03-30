from movements import possible_movements, get_random_movement
from validations import movement_within_board, visited_square, valid_move

visited_squares = [[2, 4], [1, 2], [3, 4], [4, 2]]


def test_possible_movements():
    assert [-1, 2] == possible_movements([1, 1])[0][1]
    assert [3, 2] == possible_movements([1, 1])[1][1]
    assert [3, 0] == possible_movements([1, 1])[2][1]
    assert [3, 2] == possible_movements([1, 1])[3][1]
    assert [-1, 0] == possible_movements([1, 1])[4][1]
    assert [3, 0] == possible_movements([1, 1])[5][1]
    assert [-1, 0] == possible_movements([1, 1])[6][1]
    assert [-1, 2] == possible_movements([1, 1])[7][1]


def test_movement_within_board():
    assert movement_within_board(['movement_up_right', [1, 3]])
    assert not movement_within_board(['movement_down_left', [-3, 2]])
    assert not movement_within_board(['movement_left_up', [3, -2]])
    assert not movement_within_board(['movement_down_right', [-3, -5]])


def test_visited_square():
    assert visited_square(['movement_up_right', [3, 2]], [[2, 4], [1, 2]])
    assert not visited_square(['movement_down_left', [1, 2]], [[2, 4], [1, 2]])
    assert not visited_square(['movement_left_up', [3, 4]], [[2, 4], [1, 2], [3, 4], [4, 2]])


def test_get_random_movement():
    assert 2 == len(get_random_movement([['movement_up_right', [2, 4]], ['movement_down_right', [1, 2]],
                                         ['movement_right_up', [2, 4]], ['movement_right_down', [1, 2]],
                                         ['movement_up_left', [3, 4]], ['movement_down_left', [4, 2]],
                                         ['movement_left_up', [2, 4]], ['movement_left_down', [4, 2]]
                                         ]))


def test_valid_move():
    assert valid_move(['movement_up_right', [1, 3]], visited_squares)
    assert valid_move(['movement_down_right', [1, 5]], visited_squares)
    assert not valid_move(['movement_down_left', [-3, 2]], visited_squares)
    assert not valid_move(['movement_right_up', [2, 4]], visited_squares)
    assert not valid_move(['movement_left_down', [4, 2]], visited_squares)
