product_name = input()

output = 'unknown'

if product_name in 'banana, apple, kiwi, cherry, lemon, grapes':
    output = 'fruit'

elif product_name in 'tomato, cucumber, pepper, carrot':
    output = 'vegetable'


print(output)
