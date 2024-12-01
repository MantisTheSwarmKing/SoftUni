import math
magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

price = magnolias * 3.25 + hyacinths * 4 + roses * 3.5 + cacti * 8
earning = price
earning -= (price * 0.05)

if earning < gift_price:
    print(f'She will have to borrow {math.ceil(gift_price - earning):.0f} leva.')
if earning >= gift_price:
    print(f'She is left with {math.floor(earning - gift_price):.0f} leva.')