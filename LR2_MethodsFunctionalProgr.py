<<<<<<< HEAD
# Методы функционального программирования

# 1. Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
# -------------------------------------------------------------------------------
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print("1. Используя функцию map() переписать функцию: ", squared)



# 2. Используйте функцию reduce() и перепишите код
# product = 1
# list2 = [1, 2, 3, 4]
# for num in list2:
#     product = product * num
# -------------------------------------------------------------------------------
from functools import reduce
list2 = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, list2)
print("2. Используйте функцию reduce() и перепишите код: ", product)



# 3. Используйте функцию map() и перепишите код
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)
# -------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
# Создаем функцию, которая будет возвращать квадрат числа
def square(num):
    return num ** 2
# Используем функцию map() с функцией square и списком numbers,
# результат преобразуем обратно в список
squared = list(map(square, numbers))
print("3. Используйте функцию map() и перепишите код: ", squared)



# 4. Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
x = [1, 2, 3]
y = [4, 5, 6]
# Использование функции zip()
zipped = zip(x, y)
# Преобразование результата в список
zipped_list = list(zipped)
print("4. Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip(): ", zipped_list)



# 5. Используйте функцию zip() чтобы преобразовать код:
# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])
# -------------------------------------------------------------------------------
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]
name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]
print("5. Используйте функцию zip() чтобы преобразовать код: ")
# Использование zip для объединения списков
for hero, real_name in zip(name_hero, name_real):
    print(hero, '-', real_name)



# 6. С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# Фильтрация нечетных элементов
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("6. С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.: ", odd_numbers)
=======
# Методы функционального программирования

# 1. Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
# -------------------------------------------------------------------------------
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print("1. Используя функцию map() переписать функцию: ", squared)



# 2. Используйте функцию reduce() и перепишите код
# product = 1
# list2 = [1, 2, 3, 4]
# for num in list2:
#     product = product * num
# -------------------------------------------------------------------------------
from functools import reduce
list2 = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, list2)
print("2. Используйте функцию reduce() и перепишите код: ", product)



# 3. Используйте функцию map() и перепишите код
# numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
# print(squared)
# -------------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
# Создаем функцию, которая будет возвращать квадрат числа
def square(num):
    return num ** 2
# Используем функцию map() с функцией square и списком numbers,
# результат преобразуем обратно в список
squared = list(map(square, numbers))
print("3. Используйте функцию map() и перепишите код: ", squared)



# 4. Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
x = [1, 2, 3]
y = [4, 5, 6]
# Использование функции zip()
zipped = zip(x, y)
# Преобразование результата в список
zipped_list = list(zipped)
print("4. Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip(): ", zipped_list)



# 5. Используйте функцию zip() чтобы преобразовать код:
# name_hero = [
#     'Hulk',
#     'Mr. Fantastic',
#     'Invisible Woman',
#     'Doctor Strange',
#     'Doctor Octopus',
#     'Spider-Man',
# ]
# name_real = [
#     'Bruce Banner',
#     'Reed Richards',
#     'Sue Storm',
#     'Stephen Strange',
#     'Otto Octavius',
#     'Peter Parker',
# ]
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])
# -------------------------------------------------------------------------------
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]
name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]
print("5. Используйте функцию zip() чтобы преобразовать код: ")
# Использование zip для объединения списков
for hero, real_name in zip(name_hero, name_real):
    print(hero, '-', real_name)



# 6. С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
# Фильтрация нечетных элементов
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("6. С помощью функции filter() переместите из списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.: ", odd_numbers)
>>>>>>> 9f9517e (30.05.2024)
