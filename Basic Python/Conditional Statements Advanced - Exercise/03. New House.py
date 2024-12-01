type_flower = input()
count_flower = int(input())
budget = int(input())

flower_price = 0
price_correction = 1

if type_flower == 'Roses':
    flower_price = 5

    if count_flower > 80:
        price_correction = 0.90


elif type_flower == 'Dahlias':
    flower_price = 3.80

    if count_flower > 90:
        price_correction = 0.85


elif type_flower == 'Tulips':
    flower_price = 2.80

    if count_flower > 80:
        price_correction = 0.85


elif type_flower == 'Narcissus':
    flower_price = 3

    if count_flower < 120:
        price_correction = 1.15


elif type_flower == 'Gladiolus':
    flower_price = 2.50

    if count_flower < 80:
        price_correction = 1.20

total_sum = budget - (flower_price * count_flower) * price_correction

if total_sum >= 0:
    print(f'Hey, you have a great garden with {count_flower} {type_flower} and {total_sum:.2f} leva left.')

else:
    print(f'Not enough money, you need {abs(total_sum):.2f} leva more.')
