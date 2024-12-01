import math
days = int(input())
food_left_kg = int(input())
dog_food_need_per_day_kg = float(input())
cat_food_need_per_day_kg = float(input())
tuttle_food_need_per_day_g =float(input())

total_food = days * dog_food_need_per_day_kg + days * cat_food_need_per_day_kg + days * (tuttle_food_need_per_day_g / 1000)

if total_food < food_left_kg:
    print(f'{math.floor(food_left_kg - total_food)} kilos of food left.')
if total_food >= food_left_kg:
    print(f'{math.ceil(total_food - food_left_kg)} more kilos of food are needed.')