# Task 5: Array Analysis
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

import check
import inputGenerators


def validate_list(lst):
    """
A function to check the correctness of the entered data.
    Checks that the list is not empty and contains at least two non-zero elements.
    """

    if len(lst) < 2:
        return False

    non_zero_count = 0
    for num in lst:
        if num != 0:
            non_zero_count += 1
            if non_zero_count >= 2:
                return True

    return False


def process_list(lst):
    """
A function for performing the main task with the output of the results.
    Finds the number of the maximum list item and the product of the items,
    located between the first and second non-zero elements.
    """
    max_index = lst.index(max(lst))

    product = 1
    start_index = None
    end_index = None

    for i, num in enumerate(lst):
        if num != 0:
            if start_index is None:
                start_index = i
            else:
                end_index = i
                break

    if start_index is not None and end_index is not None:
        for num in lst[start_index + 1:end_index]:
            product *= num

    return max_index, product


def print_list(lst):
    """
A function for displaying a list on the screen.
    """
    print("Список:")
    for num in lst:
        print(num)


def main():
    print("Введите элементы списка (целые числа), каждый элемент на новой строке.")
    print("Для завершения ввода введите пустую строку.")

    lst = list(inputGenerators.input_list())
    print_list(lst)

    if not validate_list(lst):
        print("Список должен содержать хотя бы два ненулевых элемента.")
        return

    max_index, product = process_list(lst)

    print("Номер максимального элемента: ", max_index)
    print("Произведение элементов между первым и вторым ненулевыми элементами: ", product)


if __name__ == "__main__":
    main()
