from src.fizzbuzz import fizz_buzz_converter


def test_when_number_is_multiple_of_3_should_return_fizz():
    assert fizz_buzz_converter(3) == "fizz"


def test_when_number_is_multiple_of_5_should_return_buzz():
    assert fizz_buzz_converter(5) == "buzz"
