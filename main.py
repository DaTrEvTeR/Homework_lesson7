import random


# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат
# повертається із функції.


# # Створюємо функцію для обчислення добутку елементів списка:
# def multiply_user_list(user_list):
#     result = 1
#     for i in user_list:
#         result *= i
#     return result
#
#
# # Генеруємо список цілих чисел та виводимо його користувачу:
# my_lst = [random.randint(1, 10) for number in range(5)]
# print(my_lst)
#
#
# # Записуємо результат обчислення добутку списку у змінну та виводимо результат користувачу:
# res = multiply_user_list(my_lst)
# print(res)


# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат
# повертається із функції.


# Створюємо функцію, яка повертає найменьше з списку
def minimum_of_user_list(user_list): return min(user_list)


# Генеруємо список цілих чисел та виводимо його користувачу:
my_lst = [random.randint(-100, 100) for number in range(20)]
print(my_lst)


# Записуємо результат у змінну та виводимо його:
res = minimum_of_user_list(my_lst)
print(res)


# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається з функції.


###


# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість
# видаленних елементів.


###


# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.


###


# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр,
# список також передається як параметр. Функція повертає новий список, який містить отримані результати.
