# In accordance with the instructions of your option, modify the program from LR3 using the class.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

import math
import statistics

import matplotlib.pyplot as plt

import TaskClass
import input_check
import repeat


class Task3(TaskClass.Task, TaskClass.TaskMixin):

    def __init__(self, task):
        """Функция, инициализирующая объект класса."""
        super().__init__(task)

    def start_task(self):
        """Функция, выполняющая основное задание."""
        rep = True
        while rep:
            # eps = input_check.float_check('\nВведите точность вычислений eps:\n', 0, float('inf'))
            x = input_check.float_check('\nВведите x в диапазоне от -1 до 1:\n', -1, 1)

            ans, n, lst = self.arccos_series(x, self.default_eps)
            print('Посчитанный вручную результат: ', ans)
            print('Посчитанный результат с помощью модуля math: ', math.acos(x))
            print('Количество итераций: ', n)
            print(f'Среднее арифметическое: {statistics.mean(lst)}')
            print(f'Медиана: {statistics.median(lst)}')
            print(f'Мода: {statistics.mode(lst)}')
            print(f'Дисперсия: {statistics.variance(lst)}')
            print(f'СКО: {statistics.stdev(lst)}')
            self.draw(1, 1000)

            rep = repeat.repeat()

    default_eps = 1e-10
    default_max_iterations = 1000000

    def compute_factorial(self, n):
        """
    A function for calculating the factorial of the number n.
        """
        factorial = 1

        if n == 0:
            return factorial

        for i in range(1, n + 1):
            factorial *= i

        return factorial

    def compute_power(self, base, exponent):
        """
    A function for raising the base number to exponent.
        """
        return base ** exponent

    def arccos_series(self, x, eps=default_eps, max_iterations=default_max_iterations):
        """
        Function to compute the value of arccos(x) using power series expansion.
        """

        result = math.pi / 2
        n = 0
        lst = []
        while n <= max_iterations:
            prev = result
            result -= self.compute_factorial(2 * n) / (self.compute_power(self.compute_factorial(2 * n), 2)) / (
                    2 * n + 1) * self.compute_power(x, 2 * n + 1)
            lst.append(result)
            n += 1

            if abs(prev - result) < eps:
                break

        return result, n, lst

    def draw(self, h, rng):
        """Функция, выполняющая построение графика с функцией варианта."""
        my_y = [self.arccos_series(elem)[0] for elem in [i / rng for i in range(-rng, rng, h)]]
        math_y = [math.acos(elem) for elem in [i / rng for i in range(-rng, rng, h)]]
        fig, ax = plt.subplots()
        ax.plot([i / rng for i in range(-rng, rng, h)], my_y, 'red', linewidth=2, label='Taylor')
        ax.plot([i / rng for i in range(-rng, rng, h)], math_y, 'blue', linewidth=2, label='Math')
        ax.legend(loc='lower left')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        # ax.text(-1.05, -2.3, 'Демонстрация графиков, полученных\nпо Тейлору и с помощью модуля Math')
        # ax.annotate('Точка, с которой начинается разложение по Тейлору', xy=(0, 0), xytext=(-0.75, 0.75),
        #             arrowprops=dict(facecolor='black', shrink=0.01))
        plt.savefig('task3.png')
        plt.show()
