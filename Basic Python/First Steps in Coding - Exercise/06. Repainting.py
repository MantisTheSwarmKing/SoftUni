

nylon_price = 1.5
paint_price = 14.50
thinner_price = 5.00
bag = 0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_total_price = float(nylon + 2) * nylon_price
paint_total_price = float(paint + (paint * (10/100))) * paint_price
thinner_total_price = float (thinner * thinner_price)
total_price_materials = nylon_total_price + paint_total_price + thinner_total_price + bag
total_price = (total_price_materials * (30/100)) * hours
all_expenses = total_price + total_price_materials

print(all_expenses)