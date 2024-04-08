import sys
# 2.1. Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
health = int(input(f'Enter value: '))
if health >= 0:
    print("Alive!")
else:
    print("Dead!")
#2.2. Напишите программу, которая проверяет является ли введенное число четным.
# Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
number = int(input('Введите любое число: '))
if number%2:
    print('Нечетное')
else:
    print('Четное')
#2.3. Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# С вложенными условиями
year = int(input())
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print('Високосный')
        else:
            print('Невисокосный')
    else:
        print('Високосный')
else:
    print('Невисокосный')
# C логическими операторами
if not year%4 and year%100 or not year%400:
    print('Високосный')
else:
    print('Невисокосный')
#2.4 Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()
# С циклом while
text = input("Enter your text: ")
num = int(input('Enter the number of repetitions: '))
i = 1
while i <= num:
    print(text)
    i += 1
# С циклом for
num = int(input('Enter the number of repetitions: '))
for i in range(1, num+1):
    print(i, text)

#2.5 Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
num1 = 0
num2 = 0
try:
    num1 = int(input('Enter number1: '))
    num2 = int(input('Enter number2: '))
except ValueError:
    print('Вы ввели не число')
    sys.exit()
operator = input('Operator: ')
if operator not in '+-*/%':
    print("Вы ввели не правильный оператор!")
    sys.exit()
if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
        print(f'{num1} {operator} {num2} = {result}')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        sys.exit()
elif num2 > 0 and operator == '/':
    result = num1 / num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '+':
    result = num1 + num2
    print(f'{num1} {operator} {num2} = {result}')
elif operator == '-':
    result = num1 - num2
    print(f'{num1} {operator} {num2} = {result}')
else:
    result = num1 * num2
    print(f'{num1} {operator} {num2} = {result}')

#solution from Aigul
num1 = int(input('Пожалуйста, введите первое число: '))
num2 = int(input('Пожалуйста, введите второе число: '))
operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
result = 0
if num2 == 0 and operator == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    sys.exit()
elif operator == '+':
    result = num1 + num2
elif operator == '*':
    result = num1 * num2
elif operator == '-':
    result = num1 - num2
elif operator == '%':
    result = num1 % num2
else:
    result = num1/num2
print(f'{num1} {operator} {num2} = {result}')