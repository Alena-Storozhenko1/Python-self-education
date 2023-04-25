print('1. Створити простий калькулятор, який зчитує три рядки введених користувачем даних: перше число, друге число та виводить операцію. ')
print('Підтримувані операції: +, -, /, *, mod, pow, div, де:')
print('mod - це отримання залишку від ділення,')
print('pow - піднесення до степеня,')
print('div - цілочисельне ділення.')



# Запит користувача на введення першого числа, другого числа та операції
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, /, *, mod, pow, div): ")

# Функція для виконання операції над двома числами
def calculate(num1, num2, operation):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "mod":
        result = num1 % num2
    elif operation == "pow":
        result = num1 ** num2
    elif operation == "div":
        result = num1 // num2
    else:
        result = "Недійсна операція"
    return result

# Виклик функції calculate та виведення результату
print(calculate(num1, num2, operation))


print('2. Маємо 2 числа a і b. Визначте, чи ділиться a на b націло. Чи ділиться b на a?')
# Запит користувача на введення двох чисел



a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

# Визначення, чи ділиться a на b націло та чи ділиться b на a
if a % b == 0:
    print(f"{a} ділиться націло на {b}")
else:
    print(f"{a} не ділиться націло на {b}")

if b % a == 0:
    print(f"{b} ділиться націло на {a}")
else:
    print(f"{b} не ділиться націло на {a}")


print('3. Дано трицифрове число. Визначте, чи є серед його цифр однакові.')



# Запит користувача на введення трьохзначного числа
num = int(input("Введіть трьохзначне число: "))

# Перетворення числа в рядок та перевірка на наявність однакових цифр
num_str = str(num)
if num_str[0] == num_str[1] or num_str[1] == num_str[2] or num_str[0] == num_str[2]:
    print(f"У числі {num} є однакові цифри")
else:
    print(f"У числі {num} немає однакових цифр")
