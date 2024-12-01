animal = input()

output = ' unknown'

if animal in 'crocodile, tortoise, snake':
    output = 'reptile'

elif animal == 'dog':
    output = 'mammal'

print(output)
