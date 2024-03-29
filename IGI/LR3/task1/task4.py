# Task 4: String Analysis
# Version 1.0
# Developed by Nikita Senko
# Date: 14.03.24

def count_vowel_words(text):
    """
A function for counting the number of words beginning or ending with a vowel letter.
    """
    vowels = "aeiouуеоаыяию"
    count = 0

    words = text.split()
    for word in words:
        if word.lower().startswith(tuple(vowels)) or word.lower().endswith(tuple(vowels)):
            count += 1

    return count


def count_character_occurrences(text):
    """
A function for counting the repetitions of each character in the text.
    """
    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


def extract_words_before_comma(text):
    """
A function for extracting words before the comma and displaying them in alphabetical order.
    """
    words = []

    for word in text.split():
        if word.endswith(","):
            words.append(word.strip(","))

    words_before_comma = sorted(words)

    return words_before_comma


def main():
    text = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy "
            "and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and "
            "picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")

    print("Использовать стандартный текст?")
    choice = input("(Да/Нет): ")
    if choice.lower() == "нет" or choice.lower() == "no" or choice.lower() == "n" or choice.lower() == "н":
        text = input("Введите текст: ")

    # a) Определить число слов, начинающихся или заканчивающихся на гласную букву
    vowel_word_count = count_vowel_words(text)
    print("Число слов, начинающихся или заканчивающихся на гласную букву:", vowel_word_count)

    # б) Определить, сколько раз повторяется каждый символ
    character_counts = count_character_occurrences(text)
    print("Повторения каждого символа:")
    for char, count in character_counts.items():
        print(f"{char}: {count}")

    # в) Вывести в алфавитном порядке слова, идущие перед запятой
    words_after_comma = extract_words_before_comma(text)
    print("Слова, идущие перед запятой в алфавитном порядке:")
    for word in sorted(words_after_comma):
        print(word)


if __name__ == "__main__":
    main()
