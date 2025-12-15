# Лабораторна робота №13

# Завдання 1
numbers = (4, 8, 15, 16, 23)

print("Перший елемент:", numbers[0])
print("Останній елемент:", numbers[-1])

# Завдання 2
student1 = ("Марія", "Іваненко")

print(f"{student1[1]} {student1[0]}")

# Завдання 3
student = {
    "ім'я": "Марія",
    "вік": 18,
    "група": "КН-21"
}

for value in student.values():
    print(value)
    
# Завдання 4
student2 = {
    "ім'я": "Марія",
    "вік": 18
}

student2["група"] = "КН-21"

print(student2)

# Завдання 5
dictionary = {
    "apple": "яблуко",
    "book": "книга",
    "cat": "кіт"
}

word = input("Введіть слово англійською: ")

if word in dictionary:
    print("Переклад:", dictionary[word])
else:
    print("Слова немає у словнику")
    
# Завдання 6
products = {
    "хліб": 25,
    "молоко": 30,
    "яйця": 60
}

total = 0

for product, price in products.items():
    quantity = int(input(f"Введіть кількість для '{product}': "))
    total += price * quantity

print("Загальна вартість:", total, "грн")
