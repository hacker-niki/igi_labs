import input_check
import repeat
import task1
import task2
import task3
import task4
import task5

tasks = [task1.Task1, task2.Task2, task3.Task3, task4.Task4, task5.Task5]


def main():
    rep = True
    while rep:
        task = input_check.int_check(
            "Задача: \n"
            "1. Задание 1\n"
            "2. Задание 2\n"
            "3. Задание 3\n"
            "4. Задание 4\n"
            "5. Задание 5\n"
            "6. Завершить программу\n",
            1, 6)
        if task == 6:
            rep = False
        else:
            tasks[task - 1](task).info()
            tasks[task - 1](task).start_task()
            rep = repeat.repeat()


if __name__ == '__main__':
    main()
