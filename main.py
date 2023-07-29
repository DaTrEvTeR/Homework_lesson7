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


# # Створюємо функцію, яка повертає найменьше з списку
# def minimum_of_user_list(user_list): return min(user_list)
#
#
# # Генеруємо список цілих чисел та виводимо його користувачу:
# my_lst = [random.randint(-100, 100) for number in range(20)]
# print(my_lst)
#
#
# # Записуємо результат у змінну та виводимо його:
# res = minimum_of_user_list(my_lst)
# print(res)


# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається з функції.


# Створюємо функцію для підрахунку к-сті простих чисел:
def count_of_simple_numbers(user_list: list) -> int: # Передаємо функції список як параметр
    counter = 0 # робимо змінну для підрахунку к-сті простих чисел
    for num in user_list: # За допомогою циклу перебираємо кожен елемент списку
        simple = True # Створюємо змінну яку будемо використовувати, для того, щоб визначати чи просте число
        if num > 2: # Прості числа це цілі числа які відрізняються від 1, та діляться з залишком тільки на себе, та на 1
            for i in range(2, num): # За допомогою циклу робимо перевірку на простоту числа
                if num % i == 0: # якщо залишок післа ділення дорівнює 0 - число складне
                    simple = False
                    break # змінюємо значення змінної та зупиняємо ітерацію цикла
            if simple: # Якщо за час перевірки зміна не змінила своє значення значить число просте
                counter += 1 # додаємо до лічильника +1 при виконанні умови
    return counter # Повертаємо обчислене значення з функції


# Генеруємо список цілих чисел та виводимо його користувачу:
my_lst = [random.randint(-100, 100) for number in range(20)]
print(my_lst)


# Записуємо результат у змінну та виводимо його:
res = count_of_simple_numbers(my_lst)
print(res)


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
