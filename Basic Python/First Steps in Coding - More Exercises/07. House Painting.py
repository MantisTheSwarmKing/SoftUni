height_house = float(input())
wight_house = float(input())
height_roof_triangle = float(input())

windows = 1.5 * 1.5
door = 1.2 * 2

house_walls = ((height_house * wight_house) * 2 - (windows * 2)) + ((height_house * height_house * 2) - door)
green_paint = house_walls / 3.4
print(f'{green_paint:.2f}')
roof = 2 * (height_house * wight_house) + 2 * (height_house  * height_roof_triangle / 2)
red_paint = roof / 4.3

print(f'{red_paint:.2f}')