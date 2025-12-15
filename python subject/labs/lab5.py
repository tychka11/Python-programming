# Лабораторна робота №5

# Завдання 1
a = 10          # int
b = 3.14        # float
c = "Привіт"    # str

print(a, type(a))
print(b, type(b))
print(c, type(c))

# Завдання 2
km = float(input("Введіть кількість кілометрів: "))
meters = km * 1000
print("Метри:", meters)

# Завдання 3
celsius = float(input("Введіть температуру в °C: "))
fahrenheit = celsius * 9 / 5 + 32
print("Температура в °F:", fahrenheit)

# Завдання 4
hours = float(input("Введіть кількість годин: "))
minutes = hours * 60
seconds = hours * 3600

print("Хвилини:", minutes)
print("Секунди:", seconds)

# Завдання 5
uah = float(input("Введіть суму в гривнях: "))
rate = float(input("Введіть курс долара: "))

usd = uah / rate
print("Сума в доларах:", usd)

# Завдання 6
cm = float(input("Введіть значення в сантиметрах: "))

meters2 = cm / 100
kilometers2 = cm / 100000

print("Метри:", meters2)
print("Кілометри:", kilometers2)