import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
# z = float(input("Введите координату z: "))

r = float(input("Введите радиус круга: "))

distance_to_origin = math.sqrt(x**2 + y**2)
# distance_to_origin = math.sqrt(x**2 + y**2 + z**2)

if distance_to_origin <= r:
    print("Точка принадлежит кругу.")
else:
    print("Точка не принадлежит кругу.")
