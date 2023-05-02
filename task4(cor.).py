import sys
import math

# Читаем первую строку, которая содержит "Задача 1.1:"
with open('input.txt', 'r', encoding='utf-8') as f:
    f.readline()
    user_input = f.readline().strip()

# Переводим ввод в число
number = int(user_input)
print('Задача 1.1 \n Введенное число:',number)

# Проверяем, попадает ли число в заданный диапазон
if (1 <= number <= 100) or (200 <= number <= 300):
    result = 'Число попадает в диапазон'
else:
    result  = 'Число не попадает в диапазон'
print(result)

with open('output.txt', 'w') as f:
    f.write('Задача 1.1\n')
    f.write(result+'\n \n')
def is_number_in_ranges(number:int)->bool:
    return (1<=number<=100) or (200<=number<=300)

#Unit test
import unittest

def test_is_number_in_ranges():
    # Test numbers within the valid ranges
    assert is_number_in_ranges(50) == True
    assert is_number_in_ranges(1) == True
    assert is_number_in_ranges(100) == True
    assert is_number_in_ranges(250) == True
    assert is_number_in_ranges(200) == True
    assert is_number_in_ranges(300) == True

    # Test numbers outside the valid ranges
    assert is_number_in_ranges(0) == False
    assert is_number_in_ranges(101) == False
    assert is_number_in_ranges(199) == False
    assert is_number_in_ranges(301) == False

    # Test border values
    assert is_number_in_ranges(1) == True
    assert is_number_in_ranges(100) == True
    assert is_number_in_ranges(200) == True
    assert is_number_in_ranges(300) == True

    print("All tests pass.")

test_is_number_in_ranges()



# Проверяем, является ли ввод числом
if not user_input.isdigit():
    print("Ошибка: Введите числовое значение.")
    exit()  # Прекращаем выполнение программы, если ввод некорректный
print('Задача 1.2')
with open('input.txt', 'r', encoding='utf-8') as f:
    f.readline()
    user_input = f.readline().strip()
# Преобразуем ввод в целое число
#temperature = int(user_input)
temp = int(input("Введите начальную температуру воды: "))
time = 0

while temp < 100:
    temp += 1
    time += 2



# Выводим результат в терминал и в файл
print(f'Вода закипит через {time} минут')
with open('output.txt', 'a') as f:
    f.write('Задача 1.2\n')
    f.write(f'Вода закипит через {time} минут\n\n')
def time_to_boil(initial_temperature):
    if not isinstance(initial_temperature, int):
        raise ValueError("Initial temperature must be an integer.")

    if initial_temperature < 0:
        raise ValueError("Initial temperature must be non-negative.")

    if initial_temperature >= 100:
        return 0

    time = 0
    while initial_temperature < 100:
        initial_temperature += 1
        time += 2

    return time


# Unit tests
import unittest
def test_time_to_boil():
    # Test with initial temperature below boiling point
    assert time_to_boil(1) == 198  # Initial temperature: 1, time to boil: 198 minutes
    assert time_to_boil(50) == 100  # Initial temperature: 50, time to boil: 100 minutes
    assert time_to_boil(99) == 2  # Initial temperature: 99, time to boil: 2 minutes

    # Test with initial temperature at boiling point
    assert time_to_boil(100) == 0  # Initial temperature: 100, time to boil: 0 minutes

    # Test with initial temperature above boiling point
    assert time_to_boil(101) == 0  # Initial temperature: 101, time to boil: 0 minutes

    # Test with non-integer initial temperature
    try:
        time_to_boil(50.5)  # Initial temperature: 50.5
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with negative initial temperature
    try:
        time_to_boil(-1)  # Initial temperature: -1
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    print("All tests pass.")


test_time_to_boil()

# Читаем число из файла input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 1.3:'):
            n = int(f.readline())
            break
print('\n Задача 1.3 \n Введенное число:')
# Выводим X строк из трех нулей
x = int(input("Введите количество строк: "))

for i in range(x):
    print(i+1, "000")
with open('output.txt', 'a') as f:
    f.write('Задача 1.3\n')
    f.write(f"{i}. 000"+'\n \n')

# Читаем число из файла input.txt
with open('input.txt', 'r',encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 1.4:'):
            n = int(f.readline())
            break

# Выводим прямоугольный треугольник
with open('output.txt', 'a') as f:
    f.write('Задача 1.4\n')
    for i in range(1, x + 1):
        triangle_line = '*' * i
        print(triangle_line)
        f.write(triangle_line + '\n')
    f.write('\n')

print('\n Задача 1.4 \n Введенное число:', x)

# Считываем размеры коробки из файла input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 2.1.'):
            box_dimensions = [int(dim) for dim in f.readline().split()]
            break

# Считываем размеры двери из файла input.txt
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Задача 2.1'):
            door_dimensions = [int(dim) for dim in f.readline().split()]
            break

a, b, c = map(int, input("Введите размеры коробки через пробел: ").split())
m, k = map(int, input("Введите размеры двери через пробел: ").split())

if a <= m and b <= k:
    print("Коробка войдет в дверь")
elif a <= m and c <= k:
    print("Коробка войдет в дверь")
elif b <= m and c <= k:
    print("Коробка войдет в дверь")
else:
    print("Коробка не войдет в дверь")

with open('output.txt', 'a') as f:
    f.write('Задача 2.1\n')
    f.write(result+'\n \n')

def does_box_fit(A, B, C, M, K):
    if not all(isinstance(dim, int) for dim in [A, B, C, M, K]):
        raise ValueError("All dimensions must be integers.")

    if any(dim <= 0 for dim in [A, B, C, M, K]):
        raise ValueError("All dimensions must be positive integers.")

    sorted_box_dims = sorted([A, B, C])
    sorted_door_dims = sorted([M, K])

    return all(box_dim <= door_dim for box_dim, door_dim in zip(sorted_box_dims, sorted_door_dims))


# Unit tests
import unittest
def test_does_box_fit():
    # Test with box that fits through the door
    assert does_box_fit(2, 3, 4, 5, 6) is True  # Box dimensions: 2x3x4, Door dimensions: 5x6

    # Test with box that does not fit through the door
    assert does_box_fit(5, 6, 7, 4, 5) is False  # Box dimensions: 5x6x7, Door dimensions: 4x5

    # Test with equal box and door dimensions
    assert does_box_fit(4, 4, 4, 4, 4) is True  # Box dimensions: 4x4x4, Door dimensions: 4x4

    # Test with non-integer dimensions
    try:
        does_box_fit(2.5, 3, 4, 5, 6)  # Box dimensions: 2.5x3x4, Door dimensions: 5x6
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with negative dimensions
    try:
        does_box_fit(2, 3, -4, 5, 6)  # Box dimensions: 2x3x-4, Door dimensions: 5x6
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    print("All tests pass.")


test_does_box_fit()

with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 2.2'):
            m = int(f.readline())
            break

    # Выводим равнобедренный треугольник из символа "*"
for i in range(1, m + 1):
    print(' ' * (m - i) + '*' * (2 * i - 1))

    # Записываем результат в файл output.txt
with open('output.txt', 'a') as f:
    f.write('Задача 2.2\n')
    for i in range(1, m + 1):
        f.write(' ' * (m - i) + '*' * (2 * i - 1) + '\n')
    f.write('\n')

# Считываем число M из файла input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 2.3:'):
            N = int(f.readline())
            break

# Генерируем последовательность квадратов чисел и выводим числа, которые меньше M

N = int(input("Введите число N: "))

squares = [x**2 for x in range(1, int(N**0.5) + 1)]
numbers = [x for x in squares if x < N]
print("Числа, которые меньше N:", numbers)

# Записываем результат в файл output.txt
with open('output.txt', 'a') as f:
    f.write('Задача 2.3\n')
    i = 1
    square = 1
    while square < N:
        f.write(str(square) + '\n')
        i += 1
        square = i ** 2
    f.write('\n')

def find_squares_less_than_N(N, squares):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("N must be a positive integer.")

    if not all(isinstance(sq, int) and sq > 0 for sq in squares):
        raise ValueError("Squares must be a sequence of positive integers.")

    return [sq for sq in squares if sq < N]


# Unit tests
import unittest
def test_find_squares_less_than_N():
    # Test with N = 5 and squares sequence: 1, 4, 9, 16, 25
    assert find_squares_less_than_N(5, [1, 4, 9, 16, 25]) == [1, 4]

    # Test with N = 10 and squares sequence: 1, 4, 9, 16, 25
    assert find_squares_less_than_N(10, [1, 4, 9, 16, 25]) == [1, 4, 9]

    # Test with N = 20 and squares sequence: 1, 4, 9, 16, 25
    assert find_squares_less_than_N(20, [1, 4, 9, 16, 25]) == [1, 4, 9, 16]

    # Test with negative N
    try:
        find_squares_less_than_N(-1, [1, 4, 9, 16, 25])
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with zero N
    try:
        find_squares_less_than_N(0, [1, 4, 9, 16, 25])
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with non-integer N
    try:
        find_squares_less_than_N(1.5, [1, 4, 9, 16, 25])
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with non-integer squares
    try:
        find_squares_less_than_N(5, [1, 4, 9, 16, 25.5])
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    print("All tests pass.")


test_find_squares_less_than_N()

# Считываем число K из файла input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 3.1:'):
            k = int(f.readline())
            break

# Проверяем возможность покупки ровно K шариков мороженого
possible = False

# Используем циклы для перебора всех возможных комбинаций
for i in range(k // 3 + 1):
    for j in range(k // 5 + 1):
        if 3 * i + 5 * j == k:
            possible = True
            break

# Выводим результат на экран и записываем его в файл output.txt
if possible:
    print(f'Можно купить ровно {k} шариков мороженого')
    with open('output.txt', 'a') as f:
        f.write(f'Задача 3.1\n')
        f.write(f'Можно купить ровно {k} шариков мороженого\n\n')
else:
    print(f'Нельзя купить ровно {k} шариков мороженого')
    with open('output.txt', 'a') as f:
        f.write(f'Задача 3.1\n')
        f.write(f'Нельзя купить ровно {k} шариков мороженого\n\n')

def can_buy_ice_cream(K):
    if not isinstance(K, int) or K < 0:
        raise ValueError("K must be a non-negative integer.")

    # Check if K can be expressed as a sum of 3's and 5's
    for i in range(K // 3 + 1):
        if (K - 3 * i) % 5 == 0:
            return True

    return False


# Unit tests
import unittest
def test_can_buy_ice_cream():
    # Test with K = 8
    assert can_buy_ice_cream(8) is True  # It is possible to buy 8 ice cream scoops

    # Test with K = 7
    assert can_buy_ice_cream(7) is False  # It is not possible to buy 7 ice cream scoops

    # Test with K = 0
    assert can_buy_ice_cream(0) is True  # It is possible to buy 0 ice cream scoops (no scoops needed)

    # Test with negative K
    try:
        can_buy_ice_cream(-1)
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with non-integer K
    try:
        can_buy_ice_cream(1.5)
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    print("All tests pass.")


test_can_buy_ice_cream()

# Считываем значения X, Y и Z из файла input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 3.2:'):
            values = f.readline().split()
            x = int(values[0])
            Y = float(values[1])
            Z = int(values[2])
            break

# Вычисляем количество лет для превышения суммы вклада Z
X = float(input("Введите сумму вклада (тысячи гривен): "))
Y = float(input("Введите процентную ставку годовых: "))
Z = float(input("Введите желаемую сумму (тысячи гривен): "))

years = 0
total_amount = X

while total_amount < Z:
    interest = total_amount * (Y / 100)
    total_amount += interest
    years += 1

# Выводим результат на экран и записываем его в файл output.txt
print(f'Сумма вклада превысит {Z} тысяч гривен через {years} лет')
with open('output.txt', 'a') as f:
    f.write('Задача 3.2\n')
    f.write(f'Сумма вклада превысит {Z} тысяч гривен через {years} лет\n\n')

def calculate_years_to_exceed_deposit(initial_deposit, annual_interest_rate, target_amount):
    if not all(isinstance(amount, (int, float)) for amount in [initial_deposit, annual_interest_rate, target_amount]):
        raise ValueError("All amounts must be numbers.")

    if any(amount <= 0 for amount in [initial_deposit, annual_interest_rate, target_amount]):
        raise ValueError("All amounts must be positive numbers.")

    years = 0
    deposit = initial_deposit

    while deposit <= target_amount:
        interest = deposit * (annual_interest_rate / 100)
        deposit += interest
        years += 1

    return years


# Unit tests
import unittest
def test_calculate_years_to_exceed_deposit():
    # Test with initial deposit of 1000, 5% annual interest rate, and target amount of 2000
    assert calculate_years_to_exceed_deposit(1000, 5, 2000) == 15

    # Test with initial deposit of 5000, 10% annual interest rate, and target amount of 10000
    assert calculate_years_to_exceed_deposit(5000, 10, 10000) == 8

    # Test with negative initial deposit
    try:
        calculate_years_to_exceed_deposit(-1000, 5, 2000)
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with zero annual interest rate
    try:
        calculate_years_to_exceed_deposit(1000, 0, 2000)
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with non-numeric input
    try:
        calculate_years_to_exceed_deposit(1000, "5", 2000)
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    print("All tests pass.")


test_calculate_years_to_exceed_deposit()

# Считываем число N из файла input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 3.3:'):
            N = int(f.readline())
            break

# Вычисляем сумму цифр числа N
sum_of_digits = 0
number = N

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

# Выводим результат на экран и записываем его в файл output.txt
print(f'Сумма цифр числа {N} равна {sum_of_digits}')
with open('output.txt', 'a') as f:
    f.write('Задача 3.3\n')
    f.write(f'Сумма цифр числа {N} равна {sum_of_digits}\n\n')

def calculate_digit_sum(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number must be a non-negative integer.")

    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)

    return digit_sum


# Unit tests
import unittest
def test_calculate_digit_sum():
    # Test with number 123
    assert calculate_digit_sum(123) == 6

    # Test with number 0
    assert calculate_digit_sum(0) == 0

    # Test with negative number
    try:
        calculate_digit_sum(-123)
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    # Test with non-integer input
    try:
        calculate_digit_sum(12.3)
        assert False  # The above statement should raise a ValueError
    except ValueError:
        assert True

    print("All tests pass.")


test_calculate_digit_sum()
