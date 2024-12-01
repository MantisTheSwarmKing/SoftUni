


pens_package_price = 5.80
materials_price = 7.20
cleaner = 1.20


pens = float(input())
materials = float(input())
board_cleaner_liters = float(input())
discount = float(input())

pens_price = pens * pens_package_price
materials_total_price = materials * materials_price
board_cleaner_price = board_cleaner_liters * cleaner
all_price = pens_price + materials_total_price + board_cleaner_price
total_price = all_price - (all_price * (discount / 100))

print(total_price)