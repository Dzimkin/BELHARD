import math

def check_point_in_round(x, y, r):
    distance_to_origin = math.sqrt(x ** 2 + y ** 2)
    # distance_to_origin = math.sqrt(x**2 + y**2 + z**2)

    if distance_to_origin <= r:
        return "Точка принадлежит кругу."
    else:
        return "Точка не принадлежит кругу."


x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
# z = float(input("Введите координату z: "))

r = float(input("Введите радиус круга: "))

result = check_point_in_round(x, y, r)
print(result)