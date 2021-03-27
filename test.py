from movements import possible_movements
from validations import movement_validation_within_board, validation_visited_squares


def test_possible_movements():
    assert [-1, 2] == possible_movements([1, 1])[0]
    assert [-1, 0] == possible_movements([1, 1])[1]
    assert [3, 2] == possible_movements([1, 1])[2]
    assert [3, 0] == possible_movements([1, 1])[3]
    assert [-1, 0] == possible_movements([1, 1])[4]
    assert [-1, 2] == possible_movements([1, 1])[5]
    assert [3, 0] == possible_movements([1, 1])[6]
    assert [3, 2] == possible_movements([1, 1])[7]


def test_movement_validation_within_board():
    assert movement_validation_within_board([1, 3])
    assert not movement_validation_within_board([-3, 2])
    assert not movement_validation_within_board([3, -2])
    assert not movement_validation_within_board([-3, -5])


def test_validation_visited_squares():
    assert validation_visited_squares([3, 2], [[2, 4], [1, 2]])
    assert not validation_visited_squares([1, 2], [[2, 4], [1, 2]])
    assert not validation_visited_squares([3, 4], [[2, 4], [1, 2], [3, 4], [4, 2]])
