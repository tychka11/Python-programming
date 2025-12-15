# Лабораторна робота №11

# Завдання 1
list_task1 = list(range(1, 11))
print("Завдання 1:", list_task1[:5])

# Завдання 2
list_task2 = list(range(1, 11))
even_task2 = list_task2[1::2]
print("Завдання 2:", even_task2)

# Завдання 3
list_task3 = [1, 2, 3, 4, 5]
reversed_task3 = list_task3[::-1]
print("Завдання 3:", reversed_task3)

# Завдання 4
strings_task4_a = ["apple", "banana", "cherry"]
strings_task4_b = ["dog", "cat", "mouse"]
combined_task4 = strings_task4_a + strings_task4_b
print("Завдання 4:", combined_task4)

# Завдання 5
list_task5 = [1, 2, 3, 4, 5]
repeated_task5 = list_task5 * 3
print("Завдання 5:", repeated_task5)

# Завдання 6
words_task6 = ["python", "java", "c++", "javascript"]
user_input_task6 = input("Введіть слово: ")
if user_input_task6 in words_task6:
    print("Завдання 6: Слово є у списку")
else:
    print("Завдання 6: Слова немає у списку")

# Завдання 7
numbers_task7 = [3, 7, 1, 9, 4]
print("Завдання 7:")
print("Мінімум:", min(numbers_task7))
print("Максимум:", max(numbers_task7))
print("Сума:", sum(numbers_task7))