# Создайте итерируемый объект,
# возвращающий генератор тридцати пяти чисел трибоначчи
# и выведите эти числа.


# ВАРИАНТ 1
def tribonacci_generator(n):
    a, b, c = 0, 1, 2
    for _ in range(n):
        # yield - ключ.слово, кот. вернёт генератор (как return, только возвращает генератор)
        yield a
        a, b, c = b, c, a + b + c

# Создаем итерируемый объект,
# возвращающий генератор тридцати пяти чисел трибоначчи
gen = tribonacci_generator(35)

# Выводим числа
for num in gen:
    print(num)



# ВАРИАНТ 2
class TribonacciGenerator:
    def __init__(self, limit):
        self.prev_prev = 0
        self.prev = 1
        self.cur = 1
        self.limit = limit
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.limit:
            result = self.prev_prev
            self.prev_prev, self.prev, self.cur = self.prev, self.cur, self.prev + self.cur + self.prev_prev
            self.i += 1
            return result
        else:
            raise StopIteration
for i in TribonacciGenerator(35):
    print(i)



#ВАРИАНТ 3
def tribonacciGenerator(limit):
    prev_prev = 0
    prev = 1
    cur = 1
    count = 0

    while count < limit:
        result = prev_prev
        prev_prev, prev, cur = prev, cur, prev + cur + prev_prev
        count += 1
        yield result


for item in tribonacciGenerator(35):
    print(item)