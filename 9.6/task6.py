import string
from collections import Counter

def letter_frequency_analysis(input_file):
    with open(input_file, 'r', encoding='cp1251') as file:
        text = file.read()

    # Очистка текста от знаков препинания и цифр
    translator = str.maketrans('', '', string.punctuation + string.digits)
    clean_text = text.translate(translator)

    # Подсчет частоты букв
    letter_count = Counter(clean_text.lower())

    # Сортировка по частоте встречаемости
    sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_letters

def main():
    input_file_path = 'C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/voina-i-mir.txt'

    result = letter_frequency_analysis(input_file_path)

    for letter, count in result:
        print(f"{letter}: {count}")

if __name__ == "__main__":
    main()

