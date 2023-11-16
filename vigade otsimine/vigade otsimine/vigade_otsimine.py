from math import sqrt, pi  # Исправил импорт

print("Ruudu karakteristikud")
a = float(input("Sisesta ruudu külje pikkus => "))  # Добавил float и исправил ковычки
S = a ** 2
print("Ruudu pindala:", S)
P = 4 * a
print("Ruudu ümbermõõt:", P) # Исправил ковычки
di = a * sqrt(2)
print("Ruudu diagonaal:", round(di, 2))
print()

print("Ristküliku karakteristikud")
b = float(input("Sisesta ristküliku 1. külje pikkus => "))  # Добавил float
c = float(input("Sisesta ristküliku 2. külje pikkus => "))  # Добавил float
S = b * c
print("Ristküliku pindala:", S)  # Добавил ковычки
P = 2 * (b + c)
print("Ristküliku ümbermõõt:", P)
di = sqrt(b ** 2 + c ** 2)
print("Ristküliku diagonaal:", round(di, 2))
print()

print("Ringi karakteristikud")
r = float(input("Sisesta ringi raadiusi pikkus => "))  # Добавил float, исправил ковычки
d = 2 * r
print("Ringi läbimõõt:", d)
S = pi * r ** 2
print("Ringi pindala:", round(S, 2))
C = 2 * pi * r
print("Ringjoone pikkus:", round(C, 2))



