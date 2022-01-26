import operations


def test_suma():
    assert operations.suma(3, 3) == 6
    assert operations.suma(-3, 3) == 0
    assert operations.suma(-3, -3) == -6
    assert operations.suma(-3, -30) == -33

def test_resta():
    assert operations.resta(3, 3) == 0
    assert operations.resta(-3, 3) == -6
    assert operations.resta(-3, -3) == 0
    assert operations.resta(-3, -30) == 27
