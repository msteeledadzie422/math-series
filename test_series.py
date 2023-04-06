from series import fibonacci, lucas, sum_series

def test_fibonacci():
    assert fibonacci


def test_lucas():
    assert lucas


def test_sum_series():
    assert sum_series


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected



def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_sum_series_lucas_five():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected


def test_sum_series_diff_series():
    actual = sum_series(5,2,3)
    expected = 21
    assert actual == expected




