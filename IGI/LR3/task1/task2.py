# Task 2: Sum of Number Sequences
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

import check


def multiply_last_digits():
    """
    Функция для нахождения суммы последовательности чисел,
    умножающихся на их последние цифры.
    """
    total = 0

    while True:
        number = check.valid_float_input("Введите целое число (0 для окончания): ")

        if number == 0:
            break

        last_digit = abs(number) % 10
        total += number * last_digit

    return total


def main():
    while True:
        total = multiply_last_digits()

        print("\nСумма последовательности чисел:", total)

        choice = input("\nХотите продолжить? (Да/Нет): ")
        if choice.lower() == "нет" or choice.lower() == "no" or choice.lower() == "n" or choice.lower() == "н":
            break


if __name__ == "__main__":
    main()
