# In accordance with the assignment of your option, explore the capabilities of the NumPy library when working with
# arrays and mathematical and static operations. Lab №4. Working with files, classes, serializers,
# regular expressions and standard libraries. Version 1.0 Developed by Nikita Senko Date: 14.03.24

import random

import numpy as np

import TaskClass
import input_check
import repeat


class Task5(TaskClass.Task):

    def __init__(self, task):
        """Функция, инициализирующая объект класса."""
        super().__init__(task)
        self.arr = None

    def start_task(self):
        """Функция, выполняющая основное задание."""
        rep = True
        while rep:
            n, m = input_check.int_check('Введите размер длину матрицы: \n', 0, 100), input_check.int_check(
                'Введите размер ширину матрицы: \n', 0, 100)
            self.arr = np.array([[random.randint(-100, 100) for i in range(n)] for j in range(m)])
            print('Получившаяся матрица:')
            print(self.arr)
            print(f'Количество четных/нечетных элементов:', self.chet_nechet())
            print('Коэффициент корреляции:', self.corrc())
            print('Коэффициент корреляции подсчитанный вручную:', self.my_corrc())

            rep = repeat.repeat()

    def chet_nechet(self):
        """Функция, подсчитывающая количество четных/нечетных элементов."""
        return len(([self.arr[i][j] for i in range(self.arr.shape[0]) for j in range(self.arr.shape[1]) if
                     self.arr[i][j] % 2 == 0])), len(
            ([self.arr[i][j] for i in range(self.arr.shape[0]) for j in range(self.arr.shape[1]) if
              self.arr[i][j] % 2 != 0]))

    def corrc(self):
        """Функция, подсчитывающая коэффициент корреляции."""

        chet = ([self.arr[i][j] for i in range(self.arr.shape[0]) for j in range(self.arr.shape[1]) if
                 self.arr[i][j] % 2 == 0])
        nechet = ([self.arr[i][j] for i in range(self.arr.shape[0]) for j in range(self.arr.shape[1]) if
                   self.arr[i][j] % 2 != 0])

        chet_len = len(chet)
        nechet_len = len(nechet)

        chet = np.resize(chet, min(chet_len, nechet_len))
        nechet = np.resize(nechet, min(chet_len, nechet_len))

        return np.corrcoef(chet, nechet)[0][1]

    def my_corrc(self):
        """Функция, подсчитывающая коэффициент корреляции вручную."""

        x = np.array([self.arr[i][j] for i in range(self.arr.shape[0]) for j in range(self.arr.shape[1]) if
                      self.arr[i][j] % 2 == 0])
        y = np.array([self.arr[i][j] for i in range(self.arr.shape[0]) for j in range(self.arr.shape[1]) if
                      self.arr[i][j] % 2 != 0])

        x_len = len(x)
        y_len = len(y)

        x = np.resize(x, min(x_len, y_len))
        y = np.resize(y, min(x_len, y_len))

        sum_xy = np.sum(x * y)
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_x_squared = np.sum(x ** 2)
        sum_y_squared = np.sum(y ** 2)

        return (len(x) * sum_xy - sum_x * sum_y) / np.sqrt(
            (len(x) * sum_x_squared - sum_x ** 2) * (len(y) * sum_y_squared - sum_y ** 2))
