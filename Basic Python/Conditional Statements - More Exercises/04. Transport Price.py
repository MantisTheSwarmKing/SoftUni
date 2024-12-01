kilometers =  int(input())
day_or_night = input()

if kilometers < 20:
    if day_or_night == 'day':
        print(f'{0.79 * kilometers + 0.70:.2f}')
    else:
        print(f'{0.90 * kilometers + 0.70:.2f}')
if 20 <= kilometers < 100:
        print(f'{0.09 * kilometers:.2f}')
if kilometers >= 100:
    print(f'{0.06 * kilometers:.2f}')
