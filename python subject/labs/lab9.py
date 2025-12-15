# Лабораторна робота №9

# Завдання 1
numbers = [3, 7, 1, 9, 5]

print("Перший елемент:", numbers[0])
print("Останній елемент:", numbers[-1])

# Завдання 2
words = ["кіт", "собака", "птах"]

words[1] = "рибка"
print(words)

# Завдання 3
fruits = ["яблуко", "банан", "апельсин"]

fruits.append("груша")
print(fruits)

# Завдання 4
numbers1 = [8, 3, 10, 1, 6]

numbers1.sort()
print(numbers1)

# Завдання 5
numbers2 = []

for i in range(5):
    num = int(input("Введіть число: "))
    numbers2.append(num)

print("Сума чисел:", sum(numbers2))

# Завдання 6
items = [4, 2, 7, 2, 9, 2, 5]

element = 2

print("Кількість входжень:", items.count(element))
print("Перша позиція:", items.index(element))