# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = float(input("Введите x - "))
y = float(input("Введите y - "))

if x > 0 and y > 0:
    print("Номер четверти - 1")
elif x > 0 and y < 0:
    print("Номер четверти - 2")
elif x < 0 and y < 0:
    print("Номер четверти - 3")
elif x < 0 and y > 0:
    print("Номер четверти - 4")
else: print("Координаты не должны равняться 0")