def validate_registration(line):
    try:
        name, email, age = line.strip().split()
        if not name.isalpha():
            raise NameError("Поле «Имя» содержит НЕ только буквы")
        if '@' not in email or '.' not in email:
            raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")
        age = int(age)
        if age < 10 or age > 99:
            raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")
    except IndexError:
        raise IndexError("НЕ присутствуют все три поля")
    
    return name, email, age

def process_registrations(input_file, good_file, bad_file):
    with open(input_file, 'r', encoding='utf-8') as file, \
        open(good_file, 'w', encoding='utf-8') as good_log, \
        open(bad_file, 'w', encoding='utf-8') as bad_log:

        for line in file:
            try:
                name, email, age = validate_registration(line)
                good_log.write(f"{name} {email} {age}\n")
            except (IndexError, NameError, SyntaxError, ValueError) as e:
                error_message = f"{line.strip()} {str(e)}\n"
                bad_log.write(error_message)
                print(error_message)

if __name__ == "__main__":
    file_path = 'C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/10.6/'

    process_registrations(file_path + 'registrations.txt', file_path + 'registrations_good.log',file_path + 'registrations_bad.log')
