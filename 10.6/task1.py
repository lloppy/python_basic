with open('C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/10.6/people.txt', 'r', encoding='utf-8') as people_file:
    name_line = people_file.read().split('\n')
    print(name_line)
    res = ''.join(name_line)
    try:
        for number, name in enumerate(name_line):
            if len(name) < 3:
                raise ValueError(f'менее трёх символов в строке {number+1}')
    except ValueError:
        print(f'менее трёх символов в строке {number+1}')
    finally:
        print(f'Общее количество символов: {len(res)}')

