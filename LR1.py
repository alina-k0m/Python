<<<<<<< HEAD
#print('hello')


# for x in range():
#     y=2**x
#     print(y)


# import numpy
# for x in range(0.0, 0.6, 0.1):
#     y=2**x
#     print(y)





# Задание 1

# Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
# m = float(input("Введите число m - "))
# n = float(input("Введите число n - "))
# p = float(input("Введите число p - "))
# negative = 0
# if m < 0:
#     negative += 1
# if n < 0:
#     negative += 1
# if p < 0:
#     negative += 1
# print("Отрицательных чисел", negative)



# Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.
# a = float(input("Введите число a - "))
# b = float(input("Введите число b - "))
# c = float(input("Введите число c - "))
#
# if a==b or b==c or a==c:
#     print("Есть как минимум одна пара равных чисел")
# else:
#     print("Равных чисел нет")



# Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля, и среднее арифметическое в противном случае.
# a = float(input("Введите число a - "))
# b = float(input("Введите число b - "))
# c = float(input("Введите число c - "))
#
# if a != 0 and b != 0 and c != 0:
#     sr_geom = (a*b*c)**(1/3)
#     print("Среднее геометрическое равно ", sr_geom)
# else:
#     sr_arifm = (a+b+c)/3
#     print("Среднее арифметическое равно ", sr_arifm)



# По номеру месяца напечатать пору года.
# month = int(input("Введите число от 1 до 12 - "))
# if month == 12 or 1 <= month <= 2:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Неверно введено число")



# Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.
# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# C = int(input("Введите число C: "))
# D = int(input("Введите число D: "))
# # Проверяем, есть ли среди них нечетное число
# if A % 2 != 0 or B % 2 != 0 or C % 2 != 0 or D % 2 != 0:
#     print("Среди заданных чисел есть нечетное.")
# else:
#     print("Среди заданных чисел нет нечетного.")


193
# Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?
# # Задаем число n
# n = int(input("Введите трехзначное натуральное число n: "))
# # Проверяем, является ли число трехзначным
# if 100 <= n <= 999:
#     # Переводим число в строку
#     n_str = str(n)
#     # Проверяем, содержит ли число цифры 0 или 9
#     if '0' in n_str or '9' in n_str:
#         print("Число содержит цифру 0 или 9.")
#     else:
#         print("Число не содержит цифр 0 или 9.")
# else:
#     print("Введено не трехзначное число.")



# В переменную Y ввести номер года. Определить, является ли год високосным.
# Y = int(input("Введите номер года: "))
# # Год високосный, если он делится на 4
# # Год високосный, если он делится на 400
# # Год не високосный, если он делится на 100
# if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
#     print(f"Год {Y} является високосным.")
# else:
#     print(f"Год {Y} не является високосным.")



# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
# n = input("Введите четырехзначное число: ")
# # Проверяем, что число четырехзначное и является натуральным
# if len(n) == 4 and n.isdigit() and int(n) > 0:
#     # Преобразуем строку в множество, чтобы убрать возможные дубликаты
#     unique_digits = set(n)
#     # Сравниваем размер множества с количеством цифр в изначальном числе
#     if len(unique_digits) == 4:
#         print(f"Все цифры числа {n} различны.")
#     else:
#         print(f"Не все цифры числа {n} различны.")
# else:
#     print("Введенное значение не является четырехзначным натуральным числом.")



# Проверить, является ли дробь A / B правильной.
# функция is_right для проверки правильности дроби
# def is_right(A, B):
#     return abs(A) < abs(B)
# # Получаем числитель и знаменатель от пользователя
# A = int(input("Введите числитель A: "))
# B = int(input("Введите знаменатель B: "))
# # Проверяем, что знаменатель не равен нулю
# if B == 0:
#     print("Знаменатель не может быть равен нулю.")
# else:
#     if is_right(A, B):
#         print(f"Дробь {A}/{B} является правильной.")
#     else:
#         print(f"Дробь {A}/{B} не является правильной.")



# Число делится на 3 тогда, когда сумма его цифр делится на 3. Проверить этот признак на примере заданного трехзначного числа.
# Функция divides_by_three для проверки, делится ли сумма цифр числа на 3
# def divides_by_three(number):
#     # Переводим число в строку
#     sum_of_digits = sum(int(digit) for digit in str(number))
#     # Проверяем, делится ли сумма цифр на 3
#     return sum_of_digits % 3 == 0
#
# number = input("Введите трехзначное число: ")
# # Проверка на трехзначность
# if len(number) == 3 and number.isdigit():
#     # Преобразование строки в число
#     number = int(number)
#     # Проверка признака делимости и вывод результата
#     if divides_by_three(number):
#         print(f"Число {number} делится на 3, так как сумма его цифр тоже делится на 3.")
#     else:
#         print(f"Число {number} не делится на 3, так как сумма его цифр не делится на 3.")
# else:
#     print("Вы ввели не трехзначное число. Пожалуйста, введите трехзначное число.")



# Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
# # Присваиваем переменной d значение наибольшего из трех чисел
# d = max(a, b, c)
# # Выводим результат
# print("Наибольшее число:", d)



# Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?
# n = int(input("Введите натуральное двузначное число n: "))
# # Преобразуем число в строку
# n_str = str(n)
# # Проверим, есть ли среди цифр числа 1 или 9
# has_1_or_9 = '1' in n_str or '9' in n_str
# print("Среди цифр числа есть 1 или 9:", has_1_or_9)



# Для натурального числа К напечатать фразу «мы нашли К грибов в лесу», согласовав окончание слова «гриб» с числом К.
# def print_mushrooms(K):
#     last_digit = K % 10
#     if 11 <= K <= 14:
#         word = "грибов"
#     elif last_digit == 1:
#         word = "гриб"
#     elif 2 <= last_digit <= 4:
#         word = "гриба"
#     else:
#         word = "грибов"
#     print(f"Мы нашли {K} {word} в лесу")
#
# K = int(input("Введите количество грибов К: "))
# print_mushrooms(K)





# Для целого числа К от 1 до 9 напечатать фразу «мне К лет», учитывая при этом,
# что при некоторых значениях К слово «лет» надо заменить на слово «год» или «года».
# def print_age(K):
#     if K == 1:
#         word = "год"
#     elif 2 <= K <= 4:
#         word = "года"
#     else:
#         word = "лет"
#     print(f"мне {K} {word}")
#
# for K in range(1, 10):
#     print_age(K)



# Определить есть ли среди заданных целых чисел A, B, C, D хотя бы одно чётное.
# def has_even_number(A, B, C, D):
#     return A % 2 == 0 or B % 2 == 0 or C % 2 == 0 or D % 2 == 0
#
# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# C = int(input("Введите число C: "))
# D = int(input("Введите число D: "))
#
# if has_even_number(A, B, C, D):
#     print("Среди чисел есть хотя бы одно чётное.")
# else:
#     print("Среди чисел нет чётных.")



# По введенному числу (от 0 до 7) напечатать название цифры.
# def print_digit_name(digit):
#     if digit < 0 or digit > 7:
#         return "Введено некорректное число. Введите число от 0 до 7."
#     names = {
#         0: "ноль",
#         1: "один",
#         2: "два",
#         3: "три",
#         4: "четыре",
#         5: "пять",
#         6: "шесть",
#         7: "семь"
#     }
#     return names[digit]
#
# # Пример использования функции
# input_digit = int(input("Введите число от 0 до 7: "))
# print(print_digit_name(input_digit))





# Задание 2

# 1. Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7. Могут ли два билета подряд быть удачными?
def is_lucky_ticket(number):
    return sum(int(digit) for digit in str(number)) % 7 == 0

def find_lucky_tickets():
    number = 100000
    while number <= 999999:
        if is_lucky_ticket(number) and is_lucky_ticket(number + 1):
            return number, number + 1
        number += 1
# как только будет найдена пара счастливых билетов, программа выведет их и завершит работу
lucky_ticket_1, lucky_ticket_2 = find_lucky_tickets()
print("Счастливый билет 1:", lucky_ticket_1)
print("Счастливый билет 2:", lucky_ticket_2)







# Задание 3

# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры.
# 1. Удалить элемент с введенным номером A.
# import random
# # Запрос размера списка
# n = int(input("Введите размер списка n: "))
#
# # Генерация списка случайных чисел в диапазоне от 0 до 99.
# A = [random.randint(0, 99) for _ in range(n)] #random.randint возвращает случайное целое в заданных пределах,
#                                                     # for _ in range(n) используется для того, чтобы повторить что-то n раз
# print("Исходный список:", A)
#
# # Запрос номера элемента для удаления
# index = int(input(f"Введите номер элемента для удаления (от 0 до {n-1}): "))
#
# # Проверка корректности введенного индекса
# if 0 <= index < n:
#     del A[index]  # Удаление элемента
#     print("Список после удаления элемента:", A)
# else:
#     print("Некорректный индекс. Элемент не может быть удален.")



# 10. Найти среднее арифметическое трех последних элементов списка
# import random
# # Запрос размера списка
# n = int(input("Введите размер списка n: "))
#
# # Генерация списка случайных чисел в диапазоне от 0 до 99.
# A = [random.randint(0, 99) for _ in range(n)] #random.randint возвращает случайное целое в заданных пределах,
#                                                     # for _ in range(n) используется для того, чтобы повторить что-то n раз
# print("Исходный список:", A)
#
# # Проверяем, достаточно ли элементов в списке, чтобы найти среднее
# if n >= 3:
#     # Вычисляем среднее арифметическое трех последних элементов
#     avg_of_last_three = sum(A[-3:]) / 3
#     print(f"Среднее арифметическое трех последних элементов списка: {avg_of_last_three}")
# else:
#     print("В списке менее трех элементов, невозможно вычислить среднее трех последних элементов.")
=======
#print('hello')


# for x in range():
#     y=2**x
#     print(y)


# import numpy
# for x in range(0.0, 0.6, 0.1):
#     y=2**x
#     print(y)





# Задание 1

# Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
# m = float(input("Введите число m - "))
# n = float(input("Введите число n - "))
# p = float(input("Введите число p - "))
# negative = 0
# if m < 0:
#     negative += 1
# if n < 0:
#     negative += 1
# if p < 0:
#     negative += 1
# print("Отрицательных чисел", negative)



# Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.
# a = float(input("Введите число a - "))
# b = float(input("Введите число b - "))
# c = float(input("Введите число c - "))
#
# if a==b or b==c or a==c:
#     print("Есть как минимум одна пара равных чисел")
# else:
#     print("Равных чисел нет")



# Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля, и среднее арифметическое в противном случае.
# a = float(input("Введите число a - "))
# b = float(input("Введите число b - "))
# c = float(input("Введите число c - "))
#
# if a != 0 and b != 0 and c != 0:
#     sr_geom = (a*b*c)**(1/3)
#     print("Среднее геометрическое равно ", sr_geom)
# else:
#     sr_arifm = (a+b+c)/3
#     print("Среднее арифметическое равно ", sr_arifm)



# По номеру месяца напечатать пору года.
# month = int(input("Введите число от 1 до 12 - "))
# if month == 12 or 1 <= month <= 2:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Неверно введено число")



# Определить, есть ли среди заданных целых чисел A, B, C, D хотя бы одно нечётное.
# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# C = int(input("Введите число C: "))
# D = int(input("Введите число D: "))
# # Проверяем, есть ли среди них нечетное число
# if A % 2 != 0 or B % 2 != 0 or C % 2 != 0 or D % 2 != 0:
#     print("Среди заданных чисел есть нечетное.")
# else:
#     print("Среди заданных чисел нет нечетного.")


193
# Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?
# # Задаем число n
# n = int(input("Введите трехзначное натуральное число n: "))
# # Проверяем, является ли число трехзначным
# if 100 <= n <= 999:
#     # Переводим число в строку
#     n_str = str(n)
#     # Проверяем, содержит ли число цифры 0 или 9
#     if '0' in n_str or '9' in n_str:
#         print("Число содержит цифру 0 или 9.")
#     else:
#         print("Число не содержит цифр 0 или 9.")
# else:
#     print("Введено не трехзначное число.")



# В переменную Y ввести номер года. Определить, является ли год високосным.
# Y = int(input("Введите номер года: "))
# # Год високосный, если он делится на 4
# # Год високосный, если он делится на 400
# # Год не високосный, если он делится на 100
# if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
#     print(f"Год {Y} является високосным.")
# else:
#     print(f"Год {Y} не является високосным.")



# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
# n = input("Введите четырехзначное число: ")
# # Проверяем, что число четырехзначное и является натуральным
# if len(n) == 4 and n.isdigit() and int(n) > 0:
#     # Преобразуем строку в множество, чтобы убрать возможные дубликаты
#     unique_digits = set(n)
#     # Сравниваем размер множества с количеством цифр в изначальном числе
#     if len(unique_digits) == 4:
#         print(f"Все цифры числа {n} различны.")
#     else:
#         print(f"Не все цифры числа {n} различны.")
# else:
#     print("Введенное значение не является четырехзначным натуральным числом.")



# Проверить, является ли дробь A / B правильной.
# функция is_right для проверки правильности дроби
# def is_right(A, B):
#     return abs(A) < abs(B)
# # Получаем числитель и знаменатель от пользователя
# A = int(input("Введите числитель A: "))
# B = int(input("Введите знаменатель B: "))
# # Проверяем, что знаменатель не равен нулю
# if B == 0:
#     print("Знаменатель не может быть равен нулю.")
# else:
#     if is_right(A, B):
#         print(f"Дробь {A}/{B} является правильной.")
#     else:
#         print(f"Дробь {A}/{B} не является правильной.")



# Число делится на 3 тогда, когда сумма его цифр делится на 3. Проверить этот признак на примере заданного трехзначного числа.
# Функция divides_by_three для проверки, делится ли сумма цифр числа на 3
# def divides_by_three(number):
#     # Переводим число в строку
#     sum_of_digits = sum(int(digit) for digit in str(number))
#     # Проверяем, делится ли сумма цифр на 3
#     return sum_of_digits % 3 == 0
#
# number = input("Введите трехзначное число: ")
# # Проверка на трехзначность
# if len(number) == 3 and number.isdigit():
#     # Преобразование строки в число
#     number = int(number)
#     # Проверка признака делимости и вывод результата
#     if divides_by_three(number):
#         print(f"Число {number} делится на 3, так как сумма его цифр тоже делится на 3.")
#     else:
#         print(f"Число {number} не делится на 3, так как сумма его цифр не делится на 3.")
# else:
#     print("Вы ввели не трехзначное число. Пожалуйста, введите трехзначное число.")



# Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
# # Присваиваем переменной d значение наибольшего из трех чисел
# d = max(a, b, c)
# # Выводим результат
# print("Наибольшее число:", d)



# Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?
# n = int(input("Введите натуральное двузначное число n: "))
# # Преобразуем число в строку
# n_str = str(n)
# # Проверим, есть ли среди цифр числа 1 или 9
# has_1_or_9 = '1' in n_str or '9' in n_str
# print("Среди цифр числа есть 1 или 9:", has_1_or_9)



# Для натурального числа К напечатать фразу «мы нашли К грибов в лесу», согласовав окончание слова «гриб» с числом К.
# def print_mushrooms(K):
#     last_digit = K % 10
#     if 11 <= K <= 14:
#         word = "грибов"
#     elif last_digit == 1:
#         word = "гриб"
#     elif 2 <= last_digit <= 4:
#         word = "гриба"
#     else:
#         word = "грибов"
#     print(f"Мы нашли {K} {word} в лесу")
#
# K = int(input("Введите количество грибов К: "))
# print_mushrooms(K)





# Для целого числа К от 1 до 9 напечатать фразу «мне К лет», учитывая при этом,
# что при некоторых значениях К слово «лет» надо заменить на слово «год» или «года».
# def print_age(K):
#     if K == 1:
#         word = "год"
#     elif 2 <= K <= 4:
#         word = "года"
#     else:
#         word = "лет"
#     print(f"мне {K} {word}")
#
# for K in range(1, 10):
#     print_age(K)



# Определить есть ли среди заданных целых чисел A, B, C, D хотя бы одно чётное.
# def has_even_number(A, B, C, D):
#     return A % 2 == 0 or B % 2 == 0 or C % 2 == 0 or D % 2 == 0
#
# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# C = int(input("Введите число C: "))
# D = int(input("Введите число D: "))
#
# if has_even_number(A, B, C, D):
#     print("Среди чисел есть хотя бы одно чётное.")
# else:
#     print("Среди чисел нет чётных.")



# По введенному числу (от 0 до 7) напечатать название цифры.
# def print_digit_name(digit):
#     if digit < 0 or digit > 7:
#         return "Введено некорректное число. Введите число от 0 до 7."
#     names = {
#         0: "ноль",
#         1: "один",
#         2: "два",
#         3: "три",
#         4: "четыре",
#         5: "пять",
#         6: "шесть",
#         7: "семь"
#     }
#     return names[digit]
#
# # Пример использования функции
# input_digit = int(input("Введите число от 0 до 7: "))
# print(print_digit_name(input_digit))





# Задание 2

# 1. Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7. Могут ли два билета подряд быть удачными?
def is_lucky_ticket(number):
    return sum(int(digit) for digit in str(number)) % 7 == 0

def find_lucky_tickets():
    number = 100000
    while number <= 999999:
        if is_lucky_ticket(number) and is_lucky_ticket(number + 1):
            return number, number + 1
        number += 1
# как только будет найдена пара счастливых билетов, программа выведет их и завершит работу
lucky_ticket_1, lucky_ticket_2 = find_lucky_tickets()
print("Счастливый билет 1:", lucky_ticket_1)
print("Счастливый билет 2:", lucky_ticket_2)







# Задание 3

# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры.
# 1. Удалить элемент с введенным номером A.
# import random
# # Запрос размера списка
# n = int(input("Введите размер списка n: "))
#
# # Генерация списка случайных чисел в диапазоне от 0 до 99.
# A = [random.randint(0, 99) for _ in range(n)] #random.randint возвращает случайное целое в заданных пределах,
#                                                     # for _ in range(n) используется для того, чтобы повторить что-то n раз
# print("Исходный список:", A)
#
# # Запрос номера элемента для удаления
# index = int(input(f"Введите номер элемента для удаления (от 0 до {n-1}): "))
#
# # Проверка корректности введенного индекса
# if 0 <= index < n:
#     del A[index]  # Удаление элемента
#     print("Список после удаления элемента:", A)
# else:
#     print("Некорректный индекс. Элемент не может быть удален.")



# 10. Найти среднее арифметическое трех последних элементов списка
# import random
# # Запрос размера списка
# n = int(input("Введите размер списка n: "))
#
# # Генерация списка случайных чисел в диапазоне от 0 до 99.
# A = [random.randint(0, 99) for _ in range(n)] #random.randint возвращает случайное целое в заданных пределах,
#                                                     # for _ in range(n) используется для того, чтобы повторить что-то n раз
# print("Исходный список:", A)
#
# # Проверяем, достаточно ли элементов в списке, чтобы найти среднее
# if n >= 3:
#     # Вычисляем среднее арифметическое трех последних элементов
#     avg_of_last_three = sum(A[-3:]) / 3
#     print(f"Среднее арифметическое трех последних элементов списка: {avg_of_last_three}")
# else:
#     print("В списке менее трех элементов, невозможно вычислить среднее трех последних элементов.")
>>>>>>> 9f9517e (30.05.2024)
