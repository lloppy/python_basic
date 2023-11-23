def filter_second_tour(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            k = int(file.readline().strip())
            participants = [line.strip().split() for line in file.readlines()]

        second_tour_participants = [participant for participant in participants if int(participant[2]) > k]
        second_tour_participants.sort(key=lambda x: int(x[2]), reverse=True)

        with open(output_file, 'w') as file:
            file.write(str(len(second_tour_participants)) + '\n')
            for i, participant in enumerate(second_tour_participants, 1):
                initials = f"{participant[1][0]}. {participant[0]}"
                file.write(f"{i}) {initials} {participant[2]}\n")

        print(f"Данные участников второго тура записаны в файл {output_file}")

    except FileNotFoundError:
        print(f"Файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

filter_second_tour(
    "C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/first_tour.txt",
      "C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/second_tour.txt"
      )
