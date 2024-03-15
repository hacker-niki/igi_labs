def is_valid_number(n) -> bool:
    """
    Функция для проверки валидности числа n.
    Возвращает True, если n является неотрицательным целым числом, и False в противном случае.
    """
    try:
        n = int(n)

    except ValueError:
        return False

    return True


def is_valid_float(n) -> bool:
    """
    Функция для проверки валидности числа n.
    Возвращает True, если n является неотрицательным целым числом, и False в противном случае.
    """
    try:
        n = float(n)
    except ValueError:
        return False

    return True


def valid_int_input(text: str) -> int:
    tmp = input(text)
    while not is_valid_number(tmp):
        print("INVALID NUMBER")
        tmp = input()

    return int(tmp)


def valid_number_input(text: str) -> float:
    tmp = input(text)
    while not is_valid_float(tmp) or float(tmp) < -1 or float(tmp) > 1:
        print("INVALID NUMBER")
        tmp = input()

    return float(tmp)


def valid_number_enter_input(text: str) -> tuple[bool, float]:
    tmp = input(text)
    if str(tmp) == "":
        return False, 0

    while not is_valid_float(tmp):
        print("INVALID NUMBER")
        tmp = input()

    return True, float(tmp)


def valid_float_input(text: str) -> float:
    tmp = input(text)
    while not is_valid_float(tmp):
        print("INVALID NUMBER")
        tmp = input()

    return float(tmp)
