# Лабораторна робота №6

# Завдання 1
num = float(input("Введіть число: "))

if num > 0:
    print("Число додатне")
else:
    print("Число не є додатним")
    
# Завдання 2
num1 = int(input("Введіть число: "))

if num1 % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")
    
# Завдання 3
age = int(input("Введіть ваш вік: "))

if age >= 18:
    print("Ви повнолітні")
else:
    print("Ви неповнолітні")
    
# Завдання 4
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if a > b:
    print("Більше число:", a)
elif b > a:
    print("Більше число:", b)
else:
    print("Числа рівні")
    
# Завдання 5
score = int(input("Введіть оцінку (1–100): "))

if score < 60:
    print("Незадовільно")
else:
    if score <= 89:
        print("Добре")
    else:
        print("Відмінно")
        
# Завдання 6
login = "admin"
password = "12345"

user_login = input("Введіть логін: ")
user_password = input("Введіть пароль: ")

if user_login == login and user_password == password:
    print("Вхід дозволено")
else:
    print("Доступ заборонено")