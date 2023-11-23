import random

def is_lucky():
    return random.randint(1, 13) == 1

def main():
    file_path = 'C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/10.6/out_file.txt'

    try:
        with open(file_path, 'w') as out_file:
            total_sum = 0

            while True:
                try:
                    user_input = input("Введите число: ")
                    number = int(user_input)
                except ValueError:
                    print("Ошибка: введите корректное число.")
                    continue

                out_file.write(str(number) + '\n')
                total_sum += number

                if is_lucky():
                    raise Exception("Вас постигла неудача!")

                if total_sum >= 777:
                    print("Вы успешно выполнили условие для выхода из порочного цикла!")
                    break

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
