from src.fizzbuzz import fizz_buzz_converter, list_factory, fizz_buzz_engine


def test_when_number_is_multiple_of_3_should_return_fizz():
    assert fizz_buzz_converter(3) == "fizz"


def test_when_number_is_multiple_of_5_should_return_buzz():
    assert fizz_buzz_converter(5) == "buzz"


def test_when_number_is_multiple_of_15_should_return_fizzbuzz():
    assert fizz_buzz_converter(15) == "fizzbuzz"


def test_when_number_is_not_multiple_of_3_5_15_should_return_number():
    assert fizz_buzz_converter(16) == "16"


def test_when_given_a_number_should_return_a_list_of_all_the_numbers_before():
    assert list_factory(16) == [x for x in range(1, 17)]


def test_when_given_a_number_should_print_a_list_of_all_the_numbers_before_converted_correctly(capsys):
    fizz_buzz_engine(16)
    captured = capsys.readouterr()
    assert captured.out == "['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11',\
 'fizz', '13', '14', 'fizzbuzz', '16']\n"
