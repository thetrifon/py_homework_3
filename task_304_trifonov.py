# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень

def my_func():
    global x, y
    x = int(input('Введите число, которое возводим в степень: '))
    y = int(input('Введите показатель степени: '))
    i = 1
    result = x
    while i < y:
        x1 = x
        result = result * x
        i += 1
    else:
        print(result)


my_result = my_func()
print(my_result)