from main import possible_movements


def test_possible_movements():
    assert [-1, 2] == possible_movements([1, 1])[0]
    assert [-1, 0] == possible_movements([1, 1])[1]
    assert [3, 2] == possible_movements([1, 1])[2]
    assert [3, 0] == possible_movements([1, 1])[3]
    assert [-1, 0] == possible_movements([1, 1])[4]
    assert [-1, 2] == possible_movements([1, 1])[5]
    assert [3, 0] == possible_movements([1, 1])[6]
    assert [3, 2] == possible_movements([1, 1])[7]
