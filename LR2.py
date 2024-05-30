<<<<<<< HEAD
# # # СОРТИРОВКА

#3 алгоритма сортировки.
# Сравнить их по времени,
# вывести в таблицу и
# построить график

import timeit
import random
import matplotlib.pyplot as plt


# Сортировка пузырьком
def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1] :
                num[j], num[j+1] = num[j+1], num[j]
    return num


# Функция сортировки выбором select
def selection_sort(num):
        # Traverse through all array elements
        for i in range(len(num)):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, len(num)):
                if num[min_idx] > num[j]:
                    min_idx = j

            # Swap the found minimum element with the first element
            num[i], num[min_idx] = num[min_idx], num[i]
        return num


# Сортировка вставками insert
def insertion_sort(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i-1
        while j >=0 and key < num[j] :
                num[j + 1] = num[j]
                j -= 1
        num[j + 1] = key
    return num


# Функция сортировки слиянием merge
def merge_sort(num):
    if len(num) > 1:
        mid = len(num) // 2  # находим середину массива

        # делим массив на две части
        L = num[:mid]
        R = num[mid:]

        # рекурсивно сортируем две половины
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # сливаем отсортированные половины в один массив
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                num[k] = L[i]
                i += 1
            else:
                num[k] = R[j]
                j += 1
            k += 1

        # проверяем, не осталось ли элементов в какой-либо из половин
        while i < len(L):
            num[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            num[k] = R[j]
            j += 1
            k += 1
        return num


# Быстрая сортировка
def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[len(num) // 2]
    left = [x for x in num if x < pivot]
    middle = [x for x in num if x == pivot]
    right = [x for x in num if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Пирамидальная сортировка (HeapSort), сортировка кучей
import heapq
def heap_sort(num):
    # Создаем кучу из итерируемого объекта
    heap = list(num)
    heapq.heapify(heap)

    # Извлекаем элементы из кучи по одному, получая их в отсортированном порядке
    return [heapq.heappop(heap) for i in range(len(heap))]


# Функция сортировки Шелла shell - модификация сортировки вставками
def shell_sort(num):
    n = len(num)
    gap = n // 2  # Начальный интервал

    # Производим сортировку с разными интервалами
    while gap > 0:
        for i in range(gap, n):
            temp = num[i]
            j = i
            # Производим сортировку вставками для этого интервала
            while j >= gap and num[j - gap] > temp:
                num[j] = num[j - gap]
                j -= gap
            num[j] = temp
        # Уменьшаем интервал
        gap //= 2
    return num


# Шейкерная сортировка
def shaker_sort(num):
    for i in range(len(num)//2):
        for j in range(len(num)-1-i):
            if num[j] > num[j+1]:
                a = num[j]
                num[j] = num[j+1]
                num[j+1] = a
        for j in range(len(num)-2-i, i+1, -1):
            if num[j] < num[j-1]:
                a = num[j]
                num[j] = num[j-1]
                num[j-1] = a
    return num


# Словарь функций сортировки
sort_functions = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort,
    'Heap Sort': heap_sort,
    'Shell Sort': shell_sort,
    'Shaker Sort': shaker_sort,
}

# Генерация наборов данных разных размеров для анализа
array_sizes = [100, 200, 300, 400, 500]
performance_results = {name: [] for name in sort_functions}

# Запуск сортировок и измерение времени исполнения
for size in array_sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    for name, sort_function in sort_functions.items():
        stmt = f'sort_function(list(data))'
        setup = f'from __main__ import sort_function, data'
        times = timeit.timeit(stmt, setup=setup, number=1)
        performance_results[name].append(times)

        print(f"{name} with array size {size}: {times:.6f} seconds")

# Создание таблицы результатов
print("\nPerformance Table:")
print(f"{'Size':<10}{' | '.join(sort_functions.keys())}")
for i, size in enumerate(array_sizes):
    results = [performance_results[name][i] for name in sort_functions]
    print(f"{size:<10}{' | '.join(f'{res:.6f}' for res in results)}")

# Построение графика производительности
plt.figure(figsize=(10, 8))
for name, times in performance_results.items():
    plt.plot(array_sizes, times, label=name)

plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()

























# import random
# import datetime
# import prettytable                  # пакет для таблицы
# import matplotlib.pyplot as plt     # библиотека для графика
#
#
# def BubbleSort(A):                  # сортировка пузырьком
#     for i in range(len(A)):
#         for j in range(len(A)-1-i):
#             if A[j] > A[j+1]:
#                 a = A[j]
#                 A[j] = A[j+1]
#                 A[j+1] = a
#
#
# def QuickSort(A, fst, lst):         # быстрая сортировка
#     if fst >= lst:
#         return
#
#     #i, j = fst, lst
#     pivot = A[fst]
#     # pivot = A[random.randint(fst, lst)]
#     first_bigger = fst+1
#     while first_bigger <= lst:
#         if A[first_bigger] >= pivot:
#             break
#         first_bigger += 1
#     i = first_bigger+1
#     while i <= lst:
#         if A[i] < pivot:
#             A[i], A[first_bigger] = A[first_bigger], A[i]
#             first_bigger += 1
#         i += 1
#
#     last_smaller = first_bigger-1
#     A[fst], A[last_smaller] = A[last_smaller], A[fst]
#     QuickSort(A, fst, last_smaller-1)
#     QuickSort(A, first_bigger, lst)
#
#
# def ShakerSort(A):                  #шейкерная (коктейльная) сортировка
#     for i in range(len(A)//2):
#         for j in range(len(A)-1-i):
#             if A[j] > A[j+1]:
#                 a = A[j]
#                 A[j] = A[j+1]
#                 A[j+1] = a
#         for j in range(len(A)-2-i, i+1, -1):
#             if A[j] < A[j-1]:
#                 a = A[j]
#                 A[j] = A[j-1]
#                 A[j-1] = a
#
#
#
# def insertion_sort(nums):                  #сортировка вставками insert
#     for i in range(1, len(nums)):
#         t = nums[i]
#         j = i
#         while j > 0 and nums[j-1] > t:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = t
#
#
#
# table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время шейкерной (коктейльной) сортировки", "Время сортировки вставками insert"]) #шапка таблицы
# x=[]
# y1=[]
# y2=[]
# y3=[]
# y4=[]
#
#
#
# for N in range(1000,5001,1000):
#     x.append(N)
#     min=1
#     max=N
#     A=[]
#     for i in range (N):
#         A.append(int(round(random.random()*(max-min)+min)))
#
#     #print(A)
#
#     B = A.copy()
#     # print(B)
#
#     C = B.copy()
#     # print(B)
#
#     D = C.copy()
#     # print(B)
#
#     # BubbleSort(A)
#     print("---")
#     # print(A)
#
#
#     # QuickSort(B, 0, len(B)-1)
#     print("---")
#     # print(B)
#
#     t1 = datetime.datetime.now()
#     BubbleSort(A)
#     t2 = datetime.datetime.now()
#     y1.append((t2-t1).total_seconds())
#     print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")
#
#     t3 = datetime.datetime.now()
#     QuickSort(B, 0, len(B)-1)
#     t4 = datetime.datetime.now()
#     y2.append((t4 - t3).total_seconds())
#     print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")
#
#     t5 = datetime.datetime.now()
#     ShakerSort(A)
#     t6 = datetime.datetime.now()
#     y2.append((t6 - t5).total_seconds())
#     print("Шейкерная   " +str(N)+"   заняла   "+str((t6-t5).total_seconds()) + "c")
#
#     t7 = datetime.datetime.now()
#     insertion_sort(nums)
#     t8 = datetime.datetime.now()
#     y2.append((t8 - t7).total_seconds())
#     print("Сортировка вставками insert   " +str(N)+"   заняла   "+str((t8-t7).total_seconds()) + "c")
#
#     table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds()), str((t8-t7).total_seconds())])
# print(table)
#
# plt.plot(x, y1, "C0")
# plt.plot(x, y2, "C1")
# plt.plot(x, y3, "C2")
# plt.plot(x, y4, "C3")
# plt.show()
#
#
#
#
#
# # 4. Функция сортировки вставками insert:
# # Цикл 1 – по i от 1 до N :					# i - текущая позиция при проходе по списку
# # 	Действие – сохранение t = A[i]		# A[i] - вставляемый элемент
# # 	Действие – новая  переменная j = i 	# j - позиция в отсортированной части списка
# # 	Цикл 2 – по j до 0 с шагом -1 :		# j - смещается справа налево, от больших к меньшим
# # 		Условие если A[j-1]>t : 			# эл-ты отсортированной части, большие вставляемого
# # 			Действие – A[j] = A[j-1] 		# уступают место – сдвигаются (копируются) вправо
# # 		Иначе – выход из цикла 2		# j остановится на посл. эл-те, большем вставляемого
# # 		Действие – A[j] = t				# вставляемый эл-т ставится на освободившееся место
=======
# # # СОРТИРОВКА

#3 алгоритма сортировки.
# Сравнить их по времени,
# вывести в таблицу и
# построить график

import timeit
import random
import matplotlib.pyplot as plt


# Сортировка пузырьком
def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1] :
                num[j], num[j+1] = num[j+1], num[j]
    return num


# Функция сортировки выбором select
def selection_sort(num):
        # Traverse through all array elements
        for i in range(len(num)):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, len(num)):
                if num[min_idx] > num[j]:
                    min_idx = j

            # Swap the found minimum element with the first element
            num[i], num[min_idx] = num[min_idx], num[i]
        return num


# Сортировка вставками insert
def insertion_sort(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i-1
        while j >=0 and key < num[j] :
                num[j + 1] = num[j]
                j -= 1
        num[j + 1] = key
    return num


# Функция сортировки слиянием merge
def merge_sort(num):
    if len(num) > 1:
        mid = len(num) // 2  # находим середину массива

        # делим массив на две части
        L = num[:mid]
        R = num[mid:]

        # рекурсивно сортируем две половины
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # сливаем отсортированные половины в один массив
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                num[k] = L[i]
                i += 1
            else:
                num[k] = R[j]
                j += 1
            k += 1

        # проверяем, не осталось ли элементов в какой-либо из половин
        while i < len(L):
            num[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            num[k] = R[j]
            j += 1
            k += 1
        return num


# Быстрая сортировка
def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[len(num) // 2]
    left = [x for x in num if x < pivot]
    middle = [x for x in num if x == pivot]
    right = [x for x in num if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Пирамидальная сортировка (HeapSort), сортировка кучей
import heapq
def heap_sort(num):
    # Создаем кучу из итерируемого объекта
    heap = list(num)
    heapq.heapify(heap)

    # Извлекаем элементы из кучи по одному, получая их в отсортированном порядке
    return [heapq.heappop(heap) for i in range(len(heap))]


# Функция сортировки Шелла shell - модификация сортировки вставками
def shell_sort(num):
    n = len(num)
    gap = n // 2  # Начальный интервал

    # Производим сортировку с разными интервалами
    while gap > 0:
        for i in range(gap, n):
            temp = num[i]
            j = i
            # Производим сортировку вставками для этого интервала
            while j >= gap and num[j - gap] > temp:
                num[j] = num[j - gap]
                j -= gap
            num[j] = temp
        # Уменьшаем интервал
        gap //= 2
    return num


# Шейкерная сортировка
def shaker_sort(num):
    for i in range(len(num)//2):
        for j in range(len(num)-1-i):
            if num[j] > num[j+1]:
                a = num[j]
                num[j] = num[j+1]
                num[j+1] = a
        for j in range(len(num)-2-i, i+1, -1):
            if num[j] < num[j-1]:
                a = num[j]
                num[j] = num[j-1]
                num[j-1] = a
    return num


# Словарь функций сортировки
sort_functions = {
    'Bubble Sort': bubble_sort,
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort,
    'Heap Sort': heap_sort,
    'Shell Sort': shell_sort,
    'Shaker Sort': shaker_sort,
}

# Генерация наборов данных разных размеров для анализа
array_sizes = [100, 200, 300, 400, 500]
performance_results = {name: [] for name in sort_functions}

# Запуск сортировок и измерение времени исполнения
for size in array_sizes:
    data = [random.randint(0, 10000) for _ in range(size)]
    for name, sort_function in sort_functions.items():
        stmt = f'sort_function(list(data))'
        setup = f'from __main__ import sort_function, data'
        times = timeit.timeit(stmt, setup=setup, number=1)
        performance_results[name].append(times)

        print(f"{name} with array size {size}: {times:.6f} seconds")

# Создание таблицы результатов
print("\nPerformance Table:")
print(f"{'Size':<10}{' | '.join(sort_functions.keys())}")
for i, size in enumerate(array_sizes):
    results = [performance_results[name][i] for name in sort_functions]
    print(f"{size:<10}{' | '.join(f'{res:.6f}' for res in results)}")

# Построение графика производительности
plt.figure(figsize=(10, 8))
for name, times in performance_results.items():
    plt.plot(array_sizes, times, label=name)

plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance Comparison')
plt.legend()
plt.grid(True)
plt.show()

























# import random
# import datetime
# import prettytable                  # пакет для таблицы
# import matplotlib.pyplot as plt     # библиотека для графика
#
#
# def BubbleSort(A):                  # сортировка пузырьком
#     for i in range(len(A)):
#         for j in range(len(A)-1-i):
#             if A[j] > A[j+1]:
#                 a = A[j]
#                 A[j] = A[j+1]
#                 A[j+1] = a
#
#
# def QuickSort(A, fst, lst):         # быстрая сортировка
#     if fst >= lst:
#         return
#
#     #i, j = fst, lst
#     pivot = A[fst]
#     # pivot = A[random.randint(fst, lst)]
#     first_bigger = fst+1
#     while first_bigger <= lst:
#         if A[first_bigger] >= pivot:
#             break
#         first_bigger += 1
#     i = first_bigger+1
#     while i <= lst:
#         if A[i] < pivot:
#             A[i], A[first_bigger] = A[first_bigger], A[i]
#             first_bigger += 1
#         i += 1
#
#     last_smaller = first_bigger-1
#     A[fst], A[last_smaller] = A[last_smaller], A[fst]
#     QuickSort(A, fst, last_smaller-1)
#     QuickSort(A, first_bigger, lst)
#
#
# def ShakerSort(A):                  #шейкерная (коктейльная) сортировка
#     for i in range(len(A)//2):
#         for j in range(len(A)-1-i):
#             if A[j] > A[j+1]:
#                 a = A[j]
#                 A[j] = A[j+1]
#                 A[j+1] = a
#         for j in range(len(A)-2-i, i+1, -1):
#             if A[j] < A[j-1]:
#                 a = A[j]
#                 A[j] = A[j-1]
#                 A[j-1] = a
#
#
#
# def insertion_sort(nums):                  #сортировка вставками insert
#     for i in range(1, len(nums)):
#         t = nums[i]
#         j = i
#         while j > 0 and nums[j-1] > t:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = t
#
#
#
# table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время шейкерной (коктейльной) сортировки", "Время сортировки вставками insert"]) #шапка таблицы
# x=[]
# y1=[]
# y2=[]
# y3=[]
# y4=[]
#
#
#
# for N in range(1000,5001,1000):
#     x.append(N)
#     min=1
#     max=N
#     A=[]
#     for i in range (N):
#         A.append(int(round(random.random()*(max-min)+min)))
#
#     #print(A)
#
#     B = A.copy()
#     # print(B)
#
#     C = B.copy()
#     # print(B)
#
#     D = C.copy()
#     # print(B)
#
#     # BubbleSort(A)
#     print("---")
#     # print(A)
#
#
#     # QuickSort(B, 0, len(B)-1)
#     print("---")
#     # print(B)
#
#     t1 = datetime.datetime.now()
#     BubbleSort(A)
#     t2 = datetime.datetime.now()
#     y1.append((t2-t1).total_seconds())
#     print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")
#
#     t3 = datetime.datetime.now()
#     QuickSort(B, 0, len(B)-1)
#     t4 = datetime.datetime.now()
#     y2.append((t4 - t3).total_seconds())
#     print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")
#
#     t5 = datetime.datetime.now()
#     ShakerSort(A)
#     t6 = datetime.datetime.now()
#     y2.append((t6 - t5).total_seconds())
#     print("Шейкерная   " +str(N)+"   заняла   "+str((t6-t5).total_seconds()) + "c")
#
#     t7 = datetime.datetime.now()
#     insertion_sort(nums)
#     t8 = datetime.datetime.now()
#     y2.append((t8 - t7).total_seconds())
#     print("Сортировка вставками insert   " +str(N)+"   заняла   "+str((t8-t7).total_seconds()) + "c")
#
#     table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds()), str((t8-t7).total_seconds())])
# print(table)
#
# plt.plot(x, y1, "C0")
# plt.plot(x, y2, "C1")
# plt.plot(x, y3, "C2")
# plt.plot(x, y4, "C3")
# plt.show()
#
#
#
#
#
# # 4. Функция сортировки вставками insert:
# # Цикл 1 – по i от 1 до N :					# i - текущая позиция при проходе по списку
# # 	Действие – сохранение t = A[i]		# A[i] - вставляемый элемент
# # 	Действие – новая  переменная j = i 	# j - позиция в отсортированной части списка
# # 	Цикл 2 – по j до 0 с шагом -1 :		# j - смещается справа налево, от больших к меньшим
# # 		Условие если A[j-1]>t : 			# эл-ты отсортированной части, большие вставляемого
# # 			Действие – A[j] = A[j-1] 		# уступают место – сдвигаются (копируются) вправо
# # 		Иначе – выход из цикла 2		# j остановится на посл. эл-те, большем вставляемого
# # 		Действие – A[j] = t				# вставляемый эл-т ставится на освободившееся место
>>>>>>> 9f9517e (30.05.2024)
