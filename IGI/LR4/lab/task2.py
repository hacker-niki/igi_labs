# In accordance with the assignment of your option, create a program for text analysis.
# Lab №4.
# Working with files, classes, serializers, regular expressions and standard libraries.
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

import re

import TaskClass
import repeat


class Task2(TaskClass.Task):
    filename = 'task2.txt'
    text = ''

    def __init__(self, task):
        """Функция, инициализирующая объект класса."""
        super().__init__(task)

    @property
    def filename_init(self):
        """Функция-геттер для переменной filename."""
        return self.filename

    @filename_init.setter
    def dict_init(self, new_filename):
        """Функция-сеттер для переменной filename."""
        self.filename = new_filename

    @property
    def text_init(self):
        """Функция-геттер для переменной text."""
        return self.filename

    @text_init.setter
    def text_init(self, new_text):
        """Функция-сеттер для переменной text."""
        self.text = new_text

    def start_task(self):
        """Функция, выполняющая основное задание."""
        rep = True
        while rep:
            self.get_text()
            self.general_task()
            self.variant_task()

            rep = repeat.repeat()

    def get_text(self):
        """Функция, которая считывает из файла данные."""
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.text = file.read()

    def general_task(self):
        """Функция, записывающая в файл результаты общего задания."""
        with open('task2_results.txt', 'w', encoding='utf-8') as file:
            file.write(f'Общее задание\n\n')
            file.write(f'Количество предложений в тексте: {self.find_sentence_count()}\n')
            file.write('\tИз них:\n')
            type_count = self.find_sentence_type_count()
            file.write(f'\tПовествовательные: {type_count[0]}\n')
            file.write(f'\tПобудительные: {type_count[1]}\n')
            file.write(f'\tВопросительные: {type_count[2]}\n')
            file.write(f'\tСредняя длина предложения: {self.find_average_sentence_len()}\n')
            file.write(f'\tСредняя длина слова: {self.find_average_word_len()}\n')
            file.write(f'\tКоличество смайликов в тексте: {self.find_smiles_count()}\n')
            file.close()

    def variant_task(self):
        """Функция, записывающая в файл результаты задания варианта."""
        with open('task2_results.txt', 'a', encoding='utf-8') as file:
            file.write('\nЗадание варианта\n\n')

            file.write('Вывести все предложения, включающие пробелы, цифры и знаки пунктуации:\n')
            for elem in self.find_sentences():
                if re.search(r"[\\s\\d\\p{P}]", elem):
                    file.write(elem + '\n')

            file.write('\n\nОпределить количество заглавных строчных букв:\n')
            uppercase_count = sum(1 for char in self.text if char.isupper())
            lowercase_count = sum(1 for char in self.text if char.islower())

            file.write(f"Количество заглавных букв:{uppercase_count}\n")
            file.write(f"Количество строчных букв:{lowercase_count}\n")

            file.write("\nПравильные даты:\n")
            for string in self.text.split():
                if self.is_valid_date(string):
                    # print(string)
                    file.write(f'{string}\n')

            file.write("\nНайти первое слово, содержащее букву 'z' и его номер")
            for index, word in enumerate(self.text.split()):
                if 'z' in word.lower():
                    file.write(f"\nПервое слово с буквой 'z':{word}\n")
                    file.write(f"Номер слова:{index}\n")
                    break

            file.write(f'Вывести строку, исключив из нее слова, начинающиеся с \'a\':\n')

            file.write(' '.join([word for word in self.text.split() if not word.lower().startswith('a')]) + "\n")
            file.close()

    def find_sentence_count(self):
        """Функция, подсчитывающая количество предложений в тексте."""
        return len(re.findall(r'[\.!?]', self.text))

    def find_sentence_type_count(self):
        """Функция, подсчитывающая количество предложений разных типов."""
        sentence_type_list = re.findall(r'[\.!?]', self.text)
        return sentence_type_list.count('.'), sentence_type_list.count('!'), sentence_type_list.count('?')

    def find_average_sentence_len(self):
        """Функция, подсчитывающая среднюю длину предложения в символах."""
        return sum(len(elem) for elem in re.findall(r'\w+', self.text)) / self.find_sentence_count()

    def find_average_word_len(self):
        """Функция, подсчитывающая среднюю длину слова в текст в символах."""
        lst = re.findall(r'\w+', self.text)
        return sum(len(elem) for elem in lst) / len(lst)

    def find_smiles_count(self):
        """Функция, подсчитывающая количество смайликов в тексте."""
        return len(re.findall(r'[:;]-*(\)+|\(+|\]+|\[+)', self.text))

    # Задания варианта
    def find_sentences(self):
        """Функция, возвращающая предложения из текста."""
        return re.findall(r'([A-Z][^.!?]*[.!?])', self.text)

    def is_valid_date(self, string):
        pattern = r"^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).((?:1[6-9]|[2-9]\d)\d{2}|9999)$"
        if re.match(pattern, string) is not None:
            return True
        else:
            return False

    def all_words(self):
        """Функция, возвращающая список всех слов в тексте."""
        return re.findall(r'\w+', self.text)
