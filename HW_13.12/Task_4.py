# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Введите номер четвети - "))
if number == 1:
    print("x > 0 \ny > 0")
elif number == 2:
    print("x > 0 \ny < 0")
elif number == 3:
    print("x < 0 \ny < 0")
elif number == 3:
    print("x < 0 \ny > 0")
else: print("Недопустимый номер четверти")