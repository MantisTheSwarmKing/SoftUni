vegetables_kg = float(input())
fruits_kg = float(input())
total_vegetables_kg = float(input())
total_fruits_kg = float(input())

earnings = vegetables_kg * total_vegetables_kg + fruits_kg * total_fruits_kg
earnings_euro = earnings / 1.94

print(f'{earnings_euro:.2f}')