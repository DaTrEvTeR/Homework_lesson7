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


# # Створюємо функцію для підрахунку к-сті простих чисел:
# def count_of_simple_numbers(user_list: list) -> int: # Передаємо функції список як параметр
#     counter = 0 # робимо змінну для підрахунку к-сті простих чисел
#     for num in user_list: # За допомогою циклу перебираємо кожен елемент списку
#         simple = True # Створюємо змінну яку будемо використовувати, для того, щоб визначати чи просте число
#         if num > 2: # Прості числа це цілі числа які відрізняються від 1, та діляться з залишком тільки на себе, та на 1
#             for i in range(2, num): # За допомогою циклу робимо перевірку на простоту числа
#                 if num % i == 0: # якщо залишок післа ділення дорівнює 0 - число складне
#                     simple = False
#                     break # змінюємо значення змінної та зупиняємо ітерацію цикла
#             if simple: # Якщо за час перевірки зміна не змінила своє значення значить число просте
#                 counter += 1 # додаємо до лічильника +1 при виконанні умови
#     return counter # Повертаємо обчислене значення з функції
#
#
# # Генеруємо список цілих чисел та виводимо його користувачу:
# my_lst = [random.randint(-100, 100) for number in range(20)]
# print(my_lst)
#
#
# # Записуємо результат у змінну та виводимо його:
# res = count_of_simple_numbers(my_lst)
# print(res)


# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість
# видаленних елементів.


# Створюємо функцію, яка видаляє всі вказані елементи зі списку та повертає к-сть видалених:
# def remove_element_from_list(my_lst, user_num): # Функція приймає список, та число яке потрібно видалити
#     copy_lst = my_lst.copy() # Копіюємо початковий список, щоб потім порівняти його з Відредагованим
#     while user_num in my_lst: # За допомогою циклу повторюємо метод ремув поки не видаляться всі елементи
#         my_lst.remove(user_num)
#     return len(copy_lst) - len(my_lst) # Повертаємо різницю довжини списку до та після редагування
#
#
# # Генеруємо список цілих чисел та виводимо його користувачу:
# my_lst = [random.randint(1, 5) for number in range(10)]
# print(my_lst)
#
# try:
#     # Запитуємо в користувача який елемент він хоче видалити:
#     user_num = int(input('Enter number to remove from list: '))
#
#
#     # Записуємо результат у змінну та виводимо його:
#     res = remove_element_from_list(my_lst, user_num)
#     print(my_lst)
#     print(f'Removed {res} elements')
# except Exception:
#     print('Ups.. some problem here, try again :)')

# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.


# def list_matches(lst1: list, lst2: list) -> list:
#     matches = [] # Створюємо список для додавання в нього елементів які є в обох списках
#     lst1_copy, lst2_copy = lst1.copy(), lst2.copy() # Робимо копії списків, щоб не втручатися в оригінали списків
#     lst1_copy, lst2_copy = set(lst1_copy), set(lst2_copy) # Переводимо списки у сети, щоб відсіяти однакові елементи
#     if len(lst1_copy) >= len(lst2_copy): # Звіряємо довжину обох списків, щоб робити менше ітерацій у циклі
#         for i in lst2_copy:
#             if i in lst1_copy:
#                 matches.append(i)
#     else:
#         for i in lst1_copy:
#             if i in lst2_copy:
#                 matches.append(i)
#     return matches # Повертаємо знайдені метчі
#
#
# # Створюємо 2 списка, та виводимо їх користувачу
# random_list_1 = [random.randint(-10, 10) for num in range(20)]
# random_list_2 = [random.randint(-10, 10) for num in range(20)]
# print(random_list_1)
# print(random_list_2)
#
#
# # Записуємо результат роботи функції у змінній та виводимо його у консоль
# res = list_matches(random_list_1, random_list_2)
# print(f'В обох списках присутні наступні елементи: {res}')


# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр,
# список також передається як параметр. Функція повертає новий список, який містить отримані результати.


# def pow_list(lst1: list, user_pow: int) -> list: # Передаємо як параметр список, та ступінь
#     lst1_powed = [] # Створюємо новий список, у який будемо заносити результат
#     for i in lst1: # За допомогою циклу зводимо у ступінь кожний елемент списку
#         lst1_powed.append(pow(i, user_pow))
#     return lst1_powed # Повертаємо з функції отриманий результат
#
#
# # Створюємо список рандомних чисел та виводимо користувачу:
# lst1 = [random.randint(-10, 10) for num in range(20)]
# print(lst1)
#
# try:
#     user_pow = int(input('Enter a pow: ')) # Запитуємо в користувача у яку ступінь зводимо всі елементи
#     res = pow_list(lst1, user_pow) # Записуємо результат в змінну та виводимо в консоль
#     print(res)
# except Exception:
#     print('Ups.. some problem here, try again :)')