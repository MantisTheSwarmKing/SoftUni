city = input()
selling_volume = float(input())


commission = 0
output = 'error'

if selling_volume < 0:
    pass

elif city == 'Sofia':

    if selling_volume <= 500:
        commission = 0.05

    elif selling_volume <= 1000:
        commission = 0.07

    elif selling_volume <= 10_000:
        commission = 0.08

    elif selling_volume > 10_000:
        commission = 0.12

elif city == 'Varna':

    if selling_volume <= 500:
        commission = 0.045

    elif selling_volume <= 1000:
        commission = 0.075

    elif selling_volume <= 10_000:
        commission = 0.10

    elif selling_volume > 10_000:
        commission = 0.13

elif city == 'Plovdiv':

    if selling_volume <= 500:
        commission = 0.055

    elif selling_volume <= 1000:
        commission = 0.08

    elif selling_volume <= 10_000:
        commission = 0.12

    elif selling_volume > 10_000:
        commission = 0.145

if commission:
    output = f'{selling_volume * commission:.2f}'
print(output)
