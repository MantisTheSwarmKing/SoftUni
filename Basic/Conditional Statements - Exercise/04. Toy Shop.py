

trip_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

total_sales = 2.60 * puzzles + 3 * talking_dolls + 4.10 * teddy_bears + 8.20 * minions + 2 * trucks

if puzzles + talking_dolls + teddy_bears + minions + trucks >= 50:
    total_sales = total_sales * 0.75

rent = total_sales * 0.10
earnings = total_sales - rent

if earnings >= trip_price:
    print(f'Yes! {earnings - trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {trip_price - earnings:.2f} lv needed.')