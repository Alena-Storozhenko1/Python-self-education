import sys
import math

# Читаем первую строку, которая содержит "Задача 1.1:" и не используем её
with open('input.txt', 'r') as f:
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


#user_input = input("Введите начальную температуру: ")

# Проверяем, является ли ввод числом
if not user_input.isdigit():
    print("Ошибка: Введите числовое значение.")
    exit()  # Прекращаем выполнение программы, если ввод некорректный
print('Задача 1.2')
with open('input.txt', 'r') as f:
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


# Читаем число из файла input.txt
with open('input.txt', 'r') as f:
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
with open('input.txt', 'r') as f:
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
with open('input.txt', 'r') as f:
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

with open('input.txt', 'r') as f:
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
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Задача 2.3:'):
            N = int(f.readline())
            break

# Генерируем последовательность квадратов чисел и выводим числа, которые меньше M
#i = 1
#square = 1
#while square < m:
    #print(square)
    #i += 1
    #square = i ** 2
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


# Считываем число K из файла input.txt
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Задача 3.3:'):
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


# Считываем значения X, Y и Z из файла input.txt
with open('input.txt', 'r') as f:
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

# Считываем число N из файла input.txt
with open('input.txt', 'r') as f:
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