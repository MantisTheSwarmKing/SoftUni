number_one = int(input())
number_two = int(input())
operator = input()


if number_one == 0 or number_two == 0:
    print(f'Cannot divide {number_one} by zero')

elif operator == '%':
    result = number_one % number_two
    print(f'{number_one} % {number_two} = {result}')

elif operator == '/':
    result = number_one / number_two
    print(f'{number_one} {operator} {number_two} = {result:.2f}')

else:
    result = eval(f'{number_one} {operator} {number_two}')

    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'

    print(f'{number_one} {operator} {number_two} = {result} - {type_number}')
