import math
squarer_meter_vineyard = int(input())
grapes_from_squarer_meter_vineyard = float(input())
liter_vine_needed = int(input())
workers = int(input())

total_grape = squarer_meter_vineyard * grapes_from_squarer_meter_vineyard
wine = total_grape * 0.40 / 2.5

if wine >= liter_vine_needed:
    left_wine = wine - liter_vine_needed
    litters_wine_per_person = left_wine / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.\n{math.ceil(left_wine)} "
          f"liters left -> {math.ceil(litters_wine_per_person)} liters per person.")
else:
    wine = abs(wine - liter_vine_needed)
    print(f"It will be a tough winter! More {math.floor(wine)} liters wine needed.")