def print_menu():
    """
    A function for printing menus.
    """
    print("Выберите задачу:")
    print("1. Вычисление значения функции arccos(x)")
    print("2. Сумма последовательности чисел")
    print("3. Анализ текста")
    print("4. Анализ строки")
    print("5. Анализ массива")
    print("0. Выход")


def main():
    while True:
        print_menu()
        choice = input("Введите номер задачи (0-5): ")

        if choice == "1":
            # Задача 1: Вычисление значения функции arccos(x)
            import task1
            task1.main()
        elif choice == "2":
            # Задача 2: Сумма последовательности чисел
            import task2
            task2.main()
        elif choice == "3":
            # Задача 3: Анализ текста
            import task3
            task3.main()
        elif choice == "4":
            # Задача 4: Анализ строки
            import task4
            task4.main()
        elif choice == "5":
            # Задача 5: Анализ массива
            import task5
            task5.main()
        elif choice == "0":
            # Выход из программы
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
