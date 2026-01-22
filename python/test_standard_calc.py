from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == 0
    assert bound_to_180(-180) == 0
    assert bound_to_180(6767) == 0
    assert bound_to_180(-6767) == 0
    assert bound_to_180(90) == 0
    assert bound_to_180(-90) == 0


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert is_angle_between(0, 50, 190)
    assert is_angle_between(0, -10, 190)
    assert is_angle_between(360, 365, 370)
    assert is_angle_between(-90, 1, -89)
    assert is_angle_between(203, 64, -3)
    assert is_angle_between(67, 6767, -67)
