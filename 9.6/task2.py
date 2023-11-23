def reverse_zen(file_path):
    try:
        with open(file_path, 'r') as file:
            zen_lines = file.readlines()

        reversed_zen = reversed(zen_lines)

        for line in reversed_zen:
            print(line.strip())

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

reverse_zen("C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/zen.txt")
