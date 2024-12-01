budget = float(input())
season = input()

destination = ''
percent_from_budget = 0
accommodation = ''

if budget <= 100:
    destination = 'Bulgaria'

    if season == 'summer':
        percent_from_budget = 0.30

    elif season == 'winter':
        percent_from_budget = 0.70

elif budget <= 1000:
    destination = 'Balkans'

    if season == 'summer':
        percent_from_budget = 0.40

    elif season == 'winter':
        percent_from_budget = 0.80

elif budget > 1000:
    destination = 'Europe'
    percent_from_budget = 0.90


if season == 'winter' or budget > 1000:
    accommodation = 'Hotel'

else:
    accommodation = 'Camp'


total_sum = budget * percent_from_budget
print(f'Somewhere in {destination}')
print(f'{accommodation} - {total_sum:.2f}')
