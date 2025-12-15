# Лабораторна робота №10

# Завдання 1
numbers = [5, 2, 9, 1, 7]

numbers.sort()
print(numbers)

# Завдання 2
numbers1 = [5, 2, 9, 1, 7]

numbers1.sort(reverse=True)
print(numbers1)

# Завдання 3
words = ["груша", "яблуко", "банан", "апельсин"]

words.sort()
print(words)

# Завдання 4
strings = ["кіт", "собака", "слон", "птах"]

strings.sort(key=len)
print(strings)

# Завдання 5
for i in range(5):
    num = int(input("Введіть число: "))
    numbers3 = []
    numbers3.append(num)

numbers3.sort()
print("Відсортований список:", numbers3)

# Завдання 6
surnames = ["Іваненко", "Петренко", "Шевчук", "Коваль"]

surnames.sort()
print("За алфавітом:", surnames)

surnames.sort(key=len)
print("За довжиною:", surnames)
