from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(-180) == -180
    assert bound_to_180(6767) == -73
    assert bound_to_180(-6767) == 73
    assert bound_to_180(90) == 90
    assert bound_to_180(-90) == -90


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert not is_angle_between(0, 50, 190)
    assert is_angle_between(0, -10, 190)
    assert is_angle_between(360, 365, 370)
    assert not is_angle_between(-90, 1, -89)
