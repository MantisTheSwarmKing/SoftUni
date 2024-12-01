resting_days = int(input())

play_time_resting_days = resting_days * 127
play_time_working_days = (365 - resting_days) * 63
total_play_time = play_time_resting_days + play_time_working_days


if total_play_time <= 30000:
    time_left = 30000 - total_play_time
    print(f'Tom sleeps well\n{time_left // 60} hours and {time_left % 60} minutes less for play')
else:
    time_left = total_play_time - 30000
    print(f'Tom will run away\n{time_left//60} hours and {time_left%60} minutes more for play')