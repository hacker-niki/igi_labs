# Serialize the dictionary and calculate the corresponding data as specified.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24


import csv
import datetime
import pickle
from datetime import date

import input_check
import repeat
from TaskClass import Task, TaskMixin


class Student:
    def __init__(self, surname, initials, birthdate):
        self.surname = surname
        self.initials = initials
        self.birthdate = birthdate

    def __str__(self):
        return f'{self.surname}, {self.initials}, {self.birthdate}'


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_average_birthday(self):
        total_days = 0
        total_months = 0
        total_years = 0

        for student in self.students:
            total_days += date.fromisoformat(str(student.birthdate)).day
            total_years += date.fromisoformat(str(student.birthdate)).year
            total_months += date.fromisoformat(str(student.birthdate)).month

        average_days = total_days / len(self.students)
        average_yars = total_years / len(self.students)
        average_months = total_months / len(self.students)

        return datetime.date(year=int(average_yars), month=int(average_months), day=int(average_days))

    def get_student(self, student_surname, student_initials):
        for student in self.students:
            if student.surname == student_surname and student.initials == student_initials:
                return student

        return Student("Not found", "Not found", datetime.date.today())


class Task1(Task, TaskMixin):

    def __init__(self, task):
        """Функция, инициализирующая объект класса."""
        super().__init__(task)
        self.schoolClass = SchoolClass()
        self.schoolClass.students = [Student("Иван", "И.И.", date(2005, 12, 22)),
                                     Student("Илья", "А.Я.", date(2005, 10, 11))]

    @property
    def students(self):
        return self.schoolClass.students

    @students.setter
    def students(self, new_list):
        self.schoolClass.students = new_list

    def start_task(self):
        """Функция, выполняющая основное задание."""
        while True:

            if input_check.int_check('Read from:\n'
                                     '1. pickle\n'
                                     '2. CSV\n',
                                     1, 2) == 1:
                self.get_pickle()
            else:
                self.get_csv()

            while True:
                var = input_check.int_check(
                    'Select which feature you want to demonstrate:\n'
                    '1. Add student\n'
                    '2. Get student\n'
                    '3. Average \n'
                    '4. Exit\n',
                    1, 4)
                if var == 1:
                    surname = input('Enter student surname: ')
                    initials = input('Enter student initials: ')
                    date_year = input_check.int_check("Enter student's date of birth (year): ")
                    date_month = input_check.int_check("Enter student's date of birth (month): ")
                    date_day = input_check.int_check("Enter student's date of birth (day): ")
                    self.schoolClass.add_student(Student(surname, initials, date(date_year, date_month, date_day)))
                elif var == 2:
                    for student in sorted(self.schoolClass.students, key=lambda student: student.surname):
                        print(student)
                    surname = input('Enter student surname: ')
                    initials = input('Enter student initials: ')
                    if self.schoolClass.get_student(surname, initials).surname != "Not found":
                        print(self.schoolClass.get_student(surname, initials))
                    else:
                        print("Student not found")
                elif var == 3:
                    print(self.schoolClass.calculate_average_birthday())
                elif var == 4:
                    self.write_all()
                    break
            if not repeat.repeat():
                break

    def get_pickle(self):
        """Функция, которая считывает из файла данные с помощью pickle."""
        with open('task1.txt', 'rb') as file:
            self.schoolClass.students = pickle.load(file)

    def get_csv(self):
        """Функция, которая считывает из файла данные с помощью CSV."""
        with open('task1.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                self.schoolClass.add_student(Student(row[0], row[1], row[2]))

    def write_all(self):
        """Функция, которая записывает в файл данные с помощью CSV и pickle."""
        with open('task1.txt', 'wb') as file:
            pickle.dump(self.schoolClass.students, file)

        with open('task1.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for student in self.schoolClass.students:
                writer.writerow([student.surname, student.initials, student.birthdate])
