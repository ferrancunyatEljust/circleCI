import operations


def test_operations():
    assert operations.suma(3, 3) == 6
    assert operations.suma(-3, 3) == 0
    assert operations.suma(-3, -3) == -6
