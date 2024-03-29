# Lab 1: Power Series Expansion of arccos(x)
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

import math
import check

default_eps = 1e-6
default_max_iterations = 500


def my_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("args:", args)
        print("result:", res)
        return res

    return wrapper


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


@my_decorator
def arccos_series(x, eps=default_eps, max_iterations=default_max_iterations):
    """
    Function to compute the value of arccos(x) using power series expansion.
    """
    result = math.pi / 2
    n = 0
    while n <= max_iterations:
        prev = result
        result -= compute_factorial(2 * n) / (compute_power(compute_factorial(2 * n), 2)) / (2 * n + 1) * compute_power(
            x, 2 * n + 1)
        n += 1

        if abs(prev - result) < eps:
            break

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
