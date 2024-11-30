day_of_the_week = input()

output = 16

if day_of_the_week in 'Monday, Tuesday, Friday':
    output = 12

elif day_of_the_week in 'Wednesday, Thursday':
    output = 14

print(output)
