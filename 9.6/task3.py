import os

def get_directory_info(directory_path):
    total_size = 0
    total_files = 0
    total_dirs = 0

    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                total_files += 1

            total_dirs += len(dirs)

        total_size_kb = total_size / 1024

        print(f"Размер каталога (в Кбайтах): {total_size_kb}")
        print(f"Количество подкаталогов: {total_dirs}")
        print(f"Количество файлов: {total_files}")

    except FileNotFoundError:
        print(f"Каталог {directory_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

get_directory_info("C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6")

# ans: 
# Размер каталога (в Кбайтах): 3.2763671875
# Количество подкаталогов: 0
# Количество файлов: 6