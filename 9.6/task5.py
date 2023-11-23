def frequency_analysis(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read().lower()

        english_letters = "abcdefghijklmnopqrstuvwxyz"
        letter_count = {letter: text.count(letter) for letter in english_letters if text.count(letter) > 0}
        total_letters = sum(letter_count.values())
        letter_percentage = {letter: count / total_letters for letter, count in letter_count.items()}

        sorted_letters = sorted(letter_percentage.items(), key=lambda x: (-x[1], x[0]))

        with open(output_file, 'w') as file:
            for letter, percentage in sorted_letters:
                file.write(f"{letter} {percentage:.3f}\n")

        print(f"Результат частотного анализа записан в файл {output_file}")

    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

frequency_analysis(
    "C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/text.txt", 
                   "C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/analysis.txt")
