# Лабораторна робота №8 

# Завдання 1
for i in range(1, 11):
    if i == 7:
        break
    print(i)
print("Цикл завершено.")

# Завдання 2
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print("Цикл завершено.")

# Завдання 3
correct_password = "1234"

while True:
    password = input("Введіть пароль: ")
    if password == correct_password:
        print("Пароль правильний!")
        break
    else:
        print("Неправильний пароль, спробуйте ще раз.")
    
# Завдання 4 
total = 0

for i in range(1, 101):
    if i % 5 == 0:
        continue
    total += i

print("Сума:", total)

# Завдання 5
x = 1

while True:
    if x > 20:
        break
    if x % 2 == 0:
        x += 1
        continue
    print(x)
    x += 1

# Завдання 6 
z = 51

while True:
    if z % 3 == 0 and z % 7 == 0:
        print("Знайдене число:", z)
        break
    z += 1