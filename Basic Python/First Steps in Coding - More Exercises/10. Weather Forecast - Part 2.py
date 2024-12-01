celsius = float(input())

if 26 <= celsius <= 35:
    print('Hot')
if 20.1 <= celsius <= 25.9:
    print('Warm')
if 15.00 <= celsius <= 20.00:
    print('Mild')
if 12.00 <= celsius <= 14.9:
    print('Cool')
if 5.00 <= celsius <= 11.9:
    print('Cold')
if celsius < 5.00 or celsius > 35:
    print('unknown')