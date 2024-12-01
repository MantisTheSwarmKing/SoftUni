type_screen_play = input()
number_rows = int(input())
number_columns = int(input())

ticket_price = 0

if type_screen_play == 'Premiere':
    ticket_price = 12

elif type_screen_play == 'Normal':
    ticket_price = 7.50

elif type_screen_play == 'Discount':
    ticket_price = 5

total_sum = ticket_price * (number_rows * number_columns)
print(f'{total_sum:.2f} leva')