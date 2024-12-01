fuel_type = input()
fuel_liters = float(input())
club_card = input()
fuel_price = 0

if fuel_type == 'Gas':
    if club_card == 'No':
        fuel_price = fuel_liters * 0.93
        if 20 <= fuel_liters <= 25:
          fuel_price *= 0.92
        if fuel_liters > 25:
            fuel_price  *= 0.90
    else:
        fuel_price = fuel_liters * (0.93 - 0.08)
        if 20 <= fuel_liters <= 25:
          fuel_price *= 0.92
        if fuel_liters > 25:
            fuel_price  *= 0.90

if fuel_type == 'Gasoline':
    if club_card == 'No':
        fuel_price = fuel_liters * 2.22
        if 20 <= fuel_liters <= 25:
          fuel_price *= 0.92
        if fuel_liters > 25:
            fuel_price  *= 0.90
    else:
        fuel_price = fuel_liters * (2.22 - 0.18)
        if 20 <= fuel_liters <= 25:
          fuel_price *= 0.92
        if fuel_liters > 25:
            fuel_price  *= 0.90

if fuel_type == 'Diesel':
    if club_card == 'No':
        fuel_price = fuel_liters * 2.33
        if 20 <= fuel_liters <= 25:
          fuel_price *= 0.92
        if fuel_liters > 25:
            fuel_price  *= 0.90
    else:
        fuel_price = fuel_liters * (2.33 - 0.12)
        if 20 <= fuel_liters <= 25:
          fuel_price *= 0.92
        if fuel_liters > 25:
            fuel_price  *= 0.90

print(f'{fuel_price:.2f} lv.')