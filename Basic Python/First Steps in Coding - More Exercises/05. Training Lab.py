from math import  floor
wight_room_meters  = float(input())
height_room_meters = float(input())

desk_in_rolls = floor(wight_room_meters * 100 / 120)
rolls = floor(((height_room_meters * 100) -  100 ) / 70)
sits = desk_in_rolls * rolls - 3
print(f'{sits}')