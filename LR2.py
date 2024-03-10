# # # сортировка
#
# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


import timeit

# Замеряем время выполнения для каждой функции сортировки
def time_sorting(sort_function, arr):
    start_time = timeit.default_timer()
    sort_function(arr.copy())
    return timeit.default_timer() - start_time

data = [5, 2, 9, 1, 5, 6]

# Измеряем время
bubble_time = time_sorting(bubble_sort, data)
insertion_time = time_sorting(insertion_sort, data)
quick_time = time_sorting(quick_sort, data)

# Составляем таблицу с помощью pandas
import pandas as pd

results = pd.DataFrame({
    'Sort Method': ['Bubble Sort', 'Insertion Sort', 'Quick Sort'],
    'Time (seconds)': [bubble_time, insertion_time, quick_time]
})

print(results)

# Построение графика
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.barh(results['Sort Method'], results['Time (seconds)'])
plt.xlabel('Time in seconds')
plt.title('Sorting Algorithms Time Comparison')
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
