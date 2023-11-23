import os

def sum_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            numbers = [int(line) for line in file.readlines()]

        total_sum = sum(numbers)
        output_path = os.path.join(os.path.dirname(input_file), output_file)

        with open(output_path, 'w') as file:
            file.write(str(total_sum))

        print(f"Сумма чисел записана в файл {output_path}")

    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

sum_numbers("C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/numbers.txt", "answer.txt")
