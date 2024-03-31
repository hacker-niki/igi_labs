# Task 2: Sum of Number Sequences
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

import inputGenerators


def multiply_last_digits():
    """
    A function for finding the sum of a sequence of numbers,
    multiplied by their last digits.
    """
    total = 1

    for number in inputGenerators.generate_int_input():
        last_digit = abs(number) % 10
        total *= last_digit

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
