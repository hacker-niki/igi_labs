import check


def generate_int_input():
    numbers: list[float] = []
    while True:
        number = check.valid_int_input("Введите число (0 для окончания): ")

        if number == 0:
            break
        numbers.append(number)

    for x in numbers:
        yield x


def input_list():
    """
    Функция для ввода элементов списка пользователем.
    """

    lst = []
    while True:
        value = check.valid_number_enter_input("Введите элемент списка: ")
        if not value[0]:
            break
        lst.append(value[1])

    for l in lst:
        yield l
