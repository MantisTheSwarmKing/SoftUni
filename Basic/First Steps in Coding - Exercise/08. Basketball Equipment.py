
year_tax = int(input())
shoes = float(year_tax - (year_tax * (40/100)))
uniform = float(shoes - (shoes * (20/100)))
ball = float(uniform * (25/100))
accessory = float(ball * (20/100))

total_price = float(year_tax + shoes + uniform + ball + accessory)

print(total_price)