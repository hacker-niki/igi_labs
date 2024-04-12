def int_check(string='', *args):
    while True:
        num = input(string)
        if isint(num):
            if len(args) == 2 and not (args[0] <= int(num) <= args[1]):
                print('\nError, enter the number in correct interval!\n')
            else:
                return int(num)
        else:
            print('\nError, enter the number!\n')


def float_check(string='', *args):
    while True:
        num = input(string)
        if isfloat(num):
            if len(args) == 2 and not (args[0] <= float(num) <= args[1]):
                print('\nError, enter the number in correct interval!\n')
            else:
                return float(num)
        else:
            print('\nError, enter the number!\n')


def isfloat(value):
    try:
        value = float(value)
        return True
    except ValueError:
        return False


def isint(value):
    try:
        value = int(value)
        return True
    except ValueError:
        return False
