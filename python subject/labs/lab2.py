#Лабораторна робота №2

#Завдання 1
name = "Дмитро"
age = 19
print("Мене звати " + name + " і мені " + str(age) + " років.")
print("Мене звати {} і мені {} років.".format(name, age))
print(f"Мене звати {name} і мені {age} років.")

#Завдання 2
for i in range(1, 11):
    print(f"7 x {i} = {7*i}")
    
#Завдання 3
import math
pi = math.pi
print(f"{pi:.2f}")
print(f"{pi:.3f}")
print(f"{pi:.5f}")

#Завдання 4
for i in range(1, 11):
    print(f"{i:4.0f} \t {i*i:4.0f}")
print("Цикл завершено.")

#Завдання 5
table = [
    ("Товар", "Кількість", "Ціна"),
    ("Банани", 15, 15.0),
    ("Мандарини", 4, 9.0),
    ("Апельсини", 6, 10.0)
]
print(f"{table[0][0]:<10} {table[0][1]:<10} {table[0][2]:<10}")
for item in table[1:]:
    print(f"{item[0]:<10} {item[1]:<10} {item[2]:<10.2f}")  
    
