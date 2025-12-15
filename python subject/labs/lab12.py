# Лабораторна робота №12

# Завдання 1
def hello(name):
    print(f"Привіт, {name}!")

hello("Марія")
hello("Олег")
hello("Анна")

# Завдання 2
def square(x):
    return x ** 2

print(square(5))

# Завдання 3
def sum_numbers(a, b):
    return a + b

print(sum_numbers(3, 7))

# Завдання 4
def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(10, 4))

# Завдання 5
def convert(celsius):
    return (9 / 5) * celsius + 32

print(convert(25))

# Завдання 6
import math

def circle(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area, circumference

area, length = circle(5)
print("Площа:", area)
print("Довжина:", length)

# Завдання 7
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))
