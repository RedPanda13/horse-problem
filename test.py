from movements import possible_movements, get_random_movement
from validations import movement_within_board, visited_square, valid_move

visited_squares = [[2, 4], [1, 2], [3, 4], [4, 2]]


def test_possible_movements():
    assert [-1, 2] == possible_movements([1, 1])[0]
    assert [3, 2] == possible_movements([1, 1])[1]
    assert [0, 3] == possible_movements([1, 1])[2]
    assert [2, 3] == possible_movements([1, 1])[3]
    assert [-1, 0] == possible_movements([1, 1])[4]
    assert [3, 0] == possible_movements([1, 1])[5]
    assert [0, -1] == possible_movements([1, 1])[6]
    assert [2, -1] == possible_movements([1, 1])[7]


def test_movement_within_board():
    assert movement_within_board([1, 3])
    assert not movement_within_board([-3, 2])
    assert not movement_within_board([3, -2])
    assert not movement_within_board([-3, -5])


def test_visited_square():
    assert visited_square([3, 2], [[2, 4], [1, 2]])
    assert not visited_square([1, 2], [[2, 4], [1, 2]])
    assert not visited_square([3, 4], [[2, 4], [1, 2], [3, 4], [4, 2]])


def test_get_random_movement():
    assert 2 == len(get_random_movement([[2, 4], [1, 2], [2, 4], [1, 2], [3, 4], [4, 2], [2, 4], [4, 2]]))


def test_valid_move():
    assert valid_move([1, 3], visited_squares)
    assert valid_move([1, 5], visited_squares)
    assert not valid_move([-3, 2], visited_squares)
    assert not valid_move([2, 4], visited_squares)
    assert not valid_move([4, 2], visited_squares)
