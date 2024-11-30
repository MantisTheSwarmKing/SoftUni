
chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50

orders_chicken = int(input())
orders_fish = int(input())
orders_vegetarian = int(input())

chicken_price = (orders_chicken * chicken_menu_price)
fish_price = (orders_fish * fish_menu_price)
vegetarian_price = (orders_vegetarian * vegetarian_menu_price)

total_price = (chicken_price + fish_price + vegetarian_price)
desert_price = (total_price * 0.20)
final_price = (total_price + desert_price + delivery_price)

print({final_price})