day = input()

output = 'Error'

if day in 'Monday, Tuesday, Wednesday, Thursday, Friday':
    output = 'Working day'

elif day in 'Saturday, Sunday':
    output = 'Weekend'


print(output)