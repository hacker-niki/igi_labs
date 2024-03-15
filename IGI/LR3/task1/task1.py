# Lab 1: Power Series Expansion of arccos(x)
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

import math
import check

default_eps = 1e-6
default_max_iterations = 500


def compute_factorial(n):
    """
    Функция для вычисления факториала числа n.
    """
    factorial = 1

    if n == 0:
        return factorial

    for i in range(1, n + 1):
        factorial *= i

    return factorial


def compute_power(base, exponent):
    """
    Функция для возведения числа base в степень exponent.
    """
    return base ** exponent


def arccos_series(x, eps=default_eps, max_iterations=default_max_iterations):
    """
    Функция для вычисления значения функции arccos(x)
    с помощью разложения в степенной ряд.
    """
    result = 0.0
    n = 0

    while True:
        numerator = compute_factorial(2 * n)
        denominator = (4 ** n) * (compute_factorial(n) ** 2) * (2 * n + 1)
        term = (numerator / denominator) * compute_power(x, 2 * n + 1)

        if n > max_iterations or abs(term) < eps:
            break

        result += term
        n += 1

    return result, n


def main():
    while True:
        x = check.valid_number_input("Введите значение аргумента (x): ")

        result, n = arccos_series(x)
        math_result = math.acos(x)

        print("\nРезультаты:")
        print("Значение аргумента (x):", x)
        print("Значение функции arccos(x):", result)
        print("Количество просуммированных членов ряда (n):", n)
        print("Значение функции arccos(x) с помощью math:", math_result)

        choice = input("\nХотите продолжить? (Да/Нет): ")
        if choice.lower() == "нет" or choice.lower() == "no" or choice.lower() == "n" or choice.lower() == "н":
            break


if __name__ == "__main__":
    main()
