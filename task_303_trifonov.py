# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func():
    global arg_1, arg_2, arg_3 #теперь переменные видны не только в функции
    arg_1 = int(input ('Введите число 1: '))
    arg_2 = int(input ('Введите число 2: '))
    arg_3 = int(input ('Введите число 3: '))
    sum_of_two = [arg_1, arg_2, arg_3]
    sum_of_two.remove(min(arg_1, arg_2, arg_3))
    return sum(sum_of_two)

my_result = my_func() #выводим результат на экран
print(my_result)



