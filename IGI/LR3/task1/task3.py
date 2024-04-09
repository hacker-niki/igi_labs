# Task 3: Text Analysis
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

def analyze_text(text):
    """
    A function for analyzing text and counting the number of spaces, numbers and punctuation marks.
    """
    space_count = 0
    digit_count = 0
    punctuation_count = 0

    for char in text:
        if char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""":
            punctuation_count += 1

    return space_count, digit_count, punctuation_count


def main():
    while True:
        input_text = input("Введите текст: ")

        space_count, digit_count, punctuation_count = analyze_text(input_text)

        print("\nРезультаты анализа текста:")
        print("Количество пробелов:", space_count)
        print("Количество цифр:", digit_count)
        print("Количество знаков пунктуации:", punctuation_count)

        choice = input("\nХотите продолжить? (Да/Нет): ")
        if choice.lower() == "нет" or choice.lower() == "no" or choice.lower() == "n" or choice.lower() == "н":
            break


if __name__ == "__main__":
    main()
