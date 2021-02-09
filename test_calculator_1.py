from calculator_1 import Calculator

# UNIT TEST FOR Calculator CLASS FROM calculator_1.py #


def test_instantiation_with_zero_as_default_calculation():
    # ARRANGE #
    calc = Calculator()

    # ACT #
    actual = calc.get_last_calculation()
    expected = 0

    # ASSERT #
    assert actual == expected


def test_instantiation_with_initial_calculation():
    # ARRANGE #
    calc = Calculator(1+1)

    # ACT #
    actual = calc.get_last_calculation()
    expected = 2

    # ASSERT #
    assert actual == expected


def test_adding_two_numbers():
    # ARRANGE #
    calc = Calculator()

    # ACT #
    actual = calc.add(1, 1)
    expected = 2

    # ASSERT #
    assert actual == expected


def test_adding_number_to_latest_calculation():
    # ARRANGE #
    calc = Calculator(1)

    # ACT #
    actual = calc.add(1)
    expected = 2

    # ASSERT #
    assert actual == expected


def test_adding_only_numbers():
    # ARRANGE #
    calc = Calculator()

    # ACT #
    actual1 = calc.add(1, "not a number")
    expected1 = "INVALID INPUT"

    actual2 = calc.add("not a number", "not a number")
    expected2 = "INVALID INPUT"

    actual3 = calc.add("not a number")
    expected3 = "INVALID INPUT"

    # ASSERT #
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3


def test_subtracting_two_numbers():
    # ARRANGE #
    calc = Calculator()

    # ACT #
    actual = calc.subtract(1, 1)
    expected = 0

    # ASSERT #
    assert actual == expected


def test_subtracting_number_from_latest_calculation():
    # ARRANGE #
    calc = Calculator(1)

    # ACT #
    actual = calc.subtract(1)
    expected = 0

    # ASSERT #
    assert actual == expected
