import math

def safe_square_root(number):
    try:
        result = math.sqrt(number)
        return result
    except ValueError as ve:
        if "math domain error" in str(ve):
            return f"Невозможно вычислить квадратный корень из отрицательного числа: {number}"
        else:
            return f"Ошибка вычисления квадратного корня: {ve}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

number1 = 25
number2 = -9

result1 = safe_square_root(number1)
result2 = safe_square_root(number2)

print(f"Квадратный корень из {number1}: {result1}")
print(f"Квадратный корень из {number2}: {result2}")
