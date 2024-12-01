budget = int(input())
season = input()
fishers = int(input())


rent = 0
discount = 1
additional_discount = 1

if season == 'Spring':
    rent = 3000

elif season in 'Summer, Autumn':
    rent = 4200

elif season == 'Winter':
    rent = 2600

if fishers <= 6:
    discount = 0.90

elif fishers <= 11:
    discount = 0.85

elif fishers >= 12:
    discount = 0.75

total_rent = rent * discount


if fishers % 2 == 0 and season != 'Autumn':
    additional_discount = 0.95


total_rent = budget - (total_rent * additional_discount)


if total_rent >= 0:
    print(f'Yes! You have {total_rent:.2f} leva left.')

else:
    print(f'Not enough money! You need {abs(total_rent):.2f} leva.')
