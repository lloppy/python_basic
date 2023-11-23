import string
from collections import Counter

def letter_frequency_analysis(input_file):
    with open(input_file, 'r', encoding='cp1251') as file:
        text = file.read()

    translator = str.maketrans('', '', string.punctuation + string.digits)
    clean_text = text.translate(translator)

    letter_count = Counter(clean_text.lower())
    srted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_letters

def main():
    input_file_path = 'C:/Users/ankud/github-classroom/UrFU-Python-GitHub-Classroom/python_basic/9.6/voina-i-mir.txt'

    result = letter_frequency_analysis(input_file_path)
    for letter, count in result:
        print(f"{letter}: {count}")

if __name__ == "__main__":
    main()

# result 
#  : 229547
# о: 131184
# а: 97839
# е: 95018
# и: 75749
# н: 75573
# т: 66898
# с: 61050
# л: 58155
# в: 52779
# р: 51223
# к: 39920
# д: 35378
# м: 34933
# у: 32184
# п: 29287
# я: 26303
# г: 23341
# ь: 23191
# ы: 22020
# б: 20531
# з: 20113
# ч: 16468

# : 15492
# й: 13403
# ж: 12046
# ш: 11266
# х: 9985
# –: 8752
#  : 7890
# ю: 7581
# e: 6271
# ц: 4090
# э: 3600
# щ: 3336
# s: 2984
# n: 2918
# i: 2852
# a: 2705
# r: 2655
# o: 2448
# u: 2448
# t: 2348
# ф: 2227
# l: 2023
# m: 1619
# c: 1295
# d: 1294
# p: 1040
# …: 989
# v: 869
# »: 667
# «: 666
# ’: 639
# h: 567
# ъ: 521
# b: 475
# q: 413
# f: 409
# g: 355
# j: 275
# x: 242
# z: 218
#         : 98
# y: 94
# k: 67
# ё: 62
# w: 39
# “: 6
# „: 6
# —: 2
