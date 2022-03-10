def fizz_buzz_converter(a: int) -> str:
    if a % 3 == 0 and a % 5 != 0:
        return "fizz"
    elif a % 5 == 0 and a % 3 != 0:
        return "buzz"
    elif a % 15 == 0:
        return "fizzbuzz"
    return str(a)


def list_factory(a: int) -> list:
    return [a]
