with open("input.txt", "w") as file:
    file.write('Задача 1.1:\n')
    file.write('1234\n')
    file.write('Задача 1.2:\n')
    file.write('7\n')
    file.write('Задача 1.3:\n')
    file.write('5\n')
    file.write('Задача 1.4:3\n4\n6\n')

    file.write('Задача 2.1\n')
    file.write('Задача 2.2:3\n4\n5\n4\n4\n')
    file.write('...\n')
import sys
output_file = open("output.txt", "w")
sys.stdout = output_file


print('Задача 1.1')

num = int(input("Введите число: "))

if (num >= 1 and num <= 100) or (num >= 200 and num <= 300):
    print("Число попадает в заданный диапазон")
else:
    print("Число не попадает в заданный диапазон")

print('Задача 1.2')

temp = int(input("Введите начальную температуру воды: "))
time = 0

while temp < 100:
    temp += 1
    time += 2

print("Вода закипит через", time, "минут")

print('Задача 1.3')

x = int(input("Введите количество строк: "))

for i in range(x):
    print(i+1, "000")

print('Задача 1.4')

with open('input.txt') as file:
    lines = file.readlines()

height = 0
for line in lines:
    if line.startswith('Задача 1.4'):
        height = int(lines[lines.index(line) + 1])
        break

for i in range(1, height + 1):
    print('*' * i)


print('Задача 2.1')

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

print('Задача 2.2')

with open('input.txt') as file:
    lines = file.readlines()

height = 0
for line in lines:
    if line.startswith('Задача 2.2'):
        height = int(lines[lines.index(line) + 1])
        break

for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))

print('Задача 2.3')
N = int(input("Введите число N: "))

squares = [x**2 for x in range(1, int(N**0.5) + 1)]
numbers = [x for x in squares if x < N]

print("Числа, которые меньше N:", numbers)

print('Задача 3.1')

k = int(input("Введите количество шариков мороженого (k): "))

if k % 3 == 0 or k % 5 == 0 or (k >= 5 and (k-5) % 3 == 0):
    print("Можно купить ровно", k, "шариков мороженого")
else:
    print("Нельзя купить ровно", k, "шариков мороженого")

print('Задача 3.2')

X = float(input("Введите сумму вклада (тысячи гривен): "))
Y = float(input("Введите процентную ставку годовых: "))
Z = float(input("Введите желаемую сумму (тысячи гривен): "))

years = 0
total_amount = X

while total_amount < Z:
    interest = total_amount * (Y / 100)
    total_amount += interest
    years += 1

print("Сумма вклада превысит", Z, "тысяч гривен через", years, "лет.")

print('Задача 3.3')

N = int(input("Введите число N: "))

squares = [x**2 for x in range(1, int(N**0.5) + 1)]
numbers = [x for x in squares if x < N]

print("Числа, которые меньше N:", numbers)

