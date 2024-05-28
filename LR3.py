# # стол
# class Table:
#     __mass = 0
#
#     def __init__(self, mass0):
#         self.__mass = mass0
#
#     # чтение инкапсулированной массы
#     def get_mass(self):
#         return self.__mass
#
# #журнальный стол
# class JournalTable(Table):
#     storage = 0
#
#
# # обеденный стол
# class DinnerTable(Table):
#     __places = 0
#
#     def __init__(self, mass0):
#         Table.__init__(self, mass0)
#         self.__places = mass0//5
#
#     # чтение инкапсулированного числа мест
#     def get_places(self):
#         return self.__places
#
#
# class Truck:
#     __maxMass = 0
#     __tables = []
#
#     def __init__(self, max_mass):
#         self.__maxMass = max_mass
#
# #расчет всех погруженных столов
#     def __current_mass(self):
#         s = 0
#         for i in self.__tables:
#             s += i.get_mass()
#         return s
#
# #расчет оставшейся доступности массы для погрузки столов
#     def reserved_mass(self):
#         return self.__maxMass - self.__current_mass()
#
#     def add_table(self, new_table):
#         if new_table.get_mass() < self.reserved_mass():
#             self.__tables.append(new_table)
#             print("Стол массой  " +
#                   str(new_table.get_mass()) +
#                   " загружен!")
#         else:
#             print("Стол массой " +
#                   str(new_table.get_mass()) +
#                   " Не влазит!\nОсталось только " +
#                   str(self.reserved_mass()) + " кг!")
#
#
# newTable = [
#     DinnerTable(10),
#     DinnerTable(20),
#     DinnerTable(30)]
#
# newTruck = Truck(50)
# newTruck.add_table(newTable[0])
# newTruck.add_table(newTable[1])
# newTruck.add_table(newTable[2])



# ------------------------------HomeWork-----------------------------------------------------------------------

# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический).
# Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.
# ДОБАВИТЬ МЕТОДЫ КЛАССА И СТАТИЧЕСКИЕ МЕТОДЫ
#
# Вар.1
# Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список книг заданного автора;
# б) список книг, выпущенных после заданного года.
class Book:
    all_books = []

    def __init__(self, id, title, authors, publisher, year, pages, price, binding_type):
        self.id = id
        self.title = title
        self.authors = authors  # Предполагается, что это список авторов
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self._price = price  # Инкапсулируем поле цены
        self.binding_type = binding_type
        Book.all_books.append(self)  # append() добавляет в конец списка элемент, переданный ему в качестве аргумента

    # Метод объекта для отображения информации о книге
    def display_info(self):
        print(f"ID: {self.id}, Title: {self.title}, Authors: {' & '.join(self.authors)}, Year: {self.year}")

    # Метод класса для вывода списка книг заданного автора
    @classmethod
    # cls — это стандартное имя первого аргумента методов класса
    def books_by_author(cls, author):
        return [book for book in cls.all_books if author in book.authors]

    # Статический метод для вывода списка книг, выпущенных после заданного года
    @staticmethod
    def books_after_year(year):
        return [book for book in Book.all_books if book.year > year]

    # Геттер для инкапсулированного поля цены
    @property
    def get_price(self):
        return self._get_price

    # Сеттер для инкапсулированного поля цены с проверкой корректности
    @get_price.setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._set_price = value


# создание списка
book1 = Book(1, "Граф Монте-Кристо", ["Александр Дюма"], "Иностранка", 2024, 670, 55.38, "Твердый переплет")
book2 = Book(2, "1984", ["Джордж Оруэлл"], "АСТ", 2022, 320, 10.70, "Мягкий переплет")
book3 = Book(3, "Мастер и Маргарита", ["Михаил Булгаков"], "Азбука", 2012, 480, 6.56, "Твердый переплет")
book4 = Book(4, "Великий Гэтсби", ["Фрэнсис Скотт Фицджеральд"], "АСТ", 2018, 256, 9.17, "Мягкий переплет")

# Вывод информации о книгах заданного автора
print("a) список книг заданного автора: ")
for book in Book.books_by_author("Александр Дюма"):
    book.display_info()

# Вывод информации о книгах, выпущенных после заданного года
print("б) список книг, выпущенных после заданного года: ")
for book in Book.books_after_year(2020):
    book.display_info()
