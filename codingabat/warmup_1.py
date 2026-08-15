def sleep_in(weekday: bool, vacation: bool) -> bool:
    return not weekday or vacation


def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    return a_smile == b_smile


def sum_double(a: int, b: int) -> int:
    sum = a + b

    if a == b:
        sum = sum * 2
    return sum


def diff21(n: int) -> int:
    if n > 21:
        return abs(n - 21) * 2
    return abs(n - 21)


def check() -> None:
    assert sleep_in(False, False)
    assert not sleep_in(True, False)

    assert monkey_trouble(True, True)
    assert monkey_trouble(False, False)

    assert sum_double(1, 2)
    assert sum_double(2, 2)

    assert diff21(19)
    assert diff21(10)


if __name__ == "__main__":
    check()
    print("all warmup-1 checks passed")
