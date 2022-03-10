def fizz_buzz_converter(a: int) -> str:
    if a % 3 == 0 and a % 5 != 0:
        return "fizz"
    elif a % 5 == 0 and a % 3 != 0:
        return "buzz"
    elif a % 15 == 0:
        return "fizzbuzz"
    return str(a)


def list_factory(a: int) -> list:
    numbers = []
    for i in range(1, a + 1):
        numbers.append(i)
    return numbers


def fizz_buzz_engine(a: int) -> list:
    numbers = list_factory(a)
    for i in range(len(numbers)):
        numbers[i] = fizz_buzz_converter(numbers[i])
    print(numbers)


