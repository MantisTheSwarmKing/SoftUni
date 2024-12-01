mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
saffron_kg = float(input())
mussels_kg = float(input())

bonito_price = mackerel_price + mackerel_price * 0.60
saffron_price = sprat_price + sprat_price * 0.80
total_price = bonito_price * bonito_kg + saffron_price * saffron_kg + mussels_kg * 7.50

print(f'{total_price:.2f}')