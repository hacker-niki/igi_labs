# In accordance with the specifications of your variant, develop base classes and descendant classes.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24


from abc import ABC, abstractmethod

import matplotlib.pyplot as plt

import TaskClass
import input_check
import repeat


class Color:
    def __init__(self, color):
        """Функция, инициализирующая объект класса."""
        self.color = color

    @property
    def color_init(self):
        """Функция-геттер для переменной color."""
        return self.color

    @color_init.setter
    def color_init(self, new_color):
        """Функция-сеттер для переменной color."""
        self.color = new_color

    @color_init.deleter
    def color_init(self):
        """Функция-делетер для переменной color."""
        del self.color

    def __str__(self):
        """Магический метод, to_string."""
        return self.color


class GeometricFigure(ABC):

    @abstractmethod
    def square(self):
        """Функция, вычисляющая площадь фигуры."""


class Trapezoid(GeometricFigure):

    def __init__(self, name, height, a, b, color):
        """Функция, инициализирующая объект класса."""
        super().__init__()
        self.height_ = height
        self.color_ = Color(color)
        self.a_ = a
        self.b_ = 2 * b - a
        self.a_, self.b_ = sorted([self.a_, self.b_])
        self.name_ = name

    @property
    def height(self):
        """Функция-геттер для переменной"""
        return self.height_

    @height.setter
    def height(self, height):
        """Функция-сеттер для переменной."""
        self.height_ = height

    @property
    def name(self):
        """Функция-геттер для переменной name."""
        return self.name_

    @name.setter
    def name(self, name):
        """Функция-сеттер для переменной name."""
        self.name_ = name

    def square(self):
        """Переопределенная функция, вычисляющая площадь трапеции."""
        return (self.a_ + self.b_) / 2 * self.height_

    def draw(self, text):
        """Функция отрисовки трапеции."""
        try:
            x = [0, (self.b_ - self.a_) / 2, (self.b_ + self.a_) / 2, self.b_, 0]
            y = [0, self.height_, self.height_, 0, 0]

            plt.legend('', frameon=False)

            plt.plot(x, y)
            plt.fill(x, y, alpha=0.3)

            plt.title(str(self.name_) + " площадь " + str(self.square()))
            plt.grid(True)
            plt.savefig('task4.png')
            plt.show()
        except ValueError:
            print('Был введен некорректный цвет')
            plt.close()

    def __str__(self):
        """Магический метод, переопределяющий __str__."""
        return 'Площадь: {}\nЦвет: {}'.format(self.square(), str(self.color_))


class Task4(TaskClass.Task):
    def __init__(self, task):
        """Функция, инициализирующая объект класса."""
        super().__init__(task)

    def start_task(self):
        """Функция, выполняющая основное задание."""
        rep = True
        while rep:
            name = input('Введите название фигуры:')
            a = input_check.float_check('Введите основание:', 0, float('inf'))
            b = input_check.float_check('Введите среднюю линию:', 0, float('inf'))
            h = input_check.float_check('Введите высоту:', 0, float('inf'))

            color = input('Введите цвет:')
            trapez = Trapezoid(name, h, a, b, color)
            trapez.draw(name)
            rep = repeat.repeat()
