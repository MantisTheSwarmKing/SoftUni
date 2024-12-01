hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_for_exam = hour_of_exam * 60 + minutes_of_exam
time_for_arrival = hour_of_arrival * 60 + minutes_of_arrival
diff = abs(time_for_exam - time_for_arrival)
hour = diff // 60
minutes = diff % 60


if time_for_exam == time_for_arrival:
    print('On Time')

if time_for_arrival != time_for_exam:
    diff = time_for_arrival - time_for_exam
    on_time = 'after'
    status = 'Late'

    if diff < 0:
        on_time = 'before'

        if diff >= -30:
            status = 'On time'
        else:
            status = 'Early'

    print(status)

    if abs(diff) // 60 == 0:
        print(f'{minutes} minutes {on_time} the start')

    else:
        print(f'{hour}:{minutes:02d} hours {on_time} the start')
