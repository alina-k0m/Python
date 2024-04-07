import io
import numpy


# главная программа:
# создание итерируемого объекта - строк файла
load_iter = io.open('food2.csv')
# преобразуем итератор в списки
lines = []
isFood = []
for line in load_iter:
    # разбиение строки на ячейки по точкам с запятой
    cells = line.split(';')
    # сохранение текущего элемента в списках
    lines += [cells[0]]
    isFood += [cells[1]]

# создаем случайную перестановку
# из порядковых номеров загруженных предметов,
# перестановка - итерируемый объект
main_iter = numpy.random.permutation(len(lines))

# вывод инструкций
print("Игра \"Съедобное-несъедобное\".")
print("Вам будут по очереди выводится названия предметов.")
print("Вводите 0 если предмет несъедобный и 1 - если съедобный.")
print("Для начала нажмите Enter.")
input()
score = 0

# проход по итерируемому объекту с помощью цикла
for num in main_iter:
    # вывод текущего элемента
    print(lines[num])
    # ввод ответа
    inbuf = input()
    # проверка правильности ответа
    if inbuf[0] == isFood[num][0]:
        print("Правильно!")
        score += 1
    else:
        print("Неправильно!")

# вывод набранных очков
print("Вы набрали " + str(score) + " очков.")
print("КОНЕЦ.")
