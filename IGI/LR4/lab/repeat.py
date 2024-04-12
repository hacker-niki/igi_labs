import input_check


def repeat():
    a = input_check.int_check('Желаете продолжить?\n'
                              '1. Да\n'
                              '2. Нет\n\n', 1, 2)
    if a == 1:
        return True
    else:
        return False
