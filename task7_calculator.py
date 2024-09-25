# Задача 7: Калькулятор с операциями
# Напишите программу, которая запрашивает у пользователя два числа и операцию (сложение, вычитание, умножение или деление) и выводит результат выполнения операции.
# Пример:
# Ввод: Первое число: 10, Второе число: 2, Операция: *
# Вывод: Результат: 20
first, second, operation = input("Введите 2 числа и операцию: ").split()
first, second = int(first), int(second)
if operation == '+':
    print(f'Результат: {first + second}')
elif operation == '-':
    print(f'Результат: {first - second}')
elif operation == '*':
    print(f'Результат: {first * second}')
elif operation == '/':
    print(f'Результат: {first / second}')