

from math import ceil

movie = str(input())
movie_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
relax_time = break_time / 4

available_time = break_time - lunch_time - relax_time
diff = abs(movie_time - available_time)

if movie_time > available_time:
    print(f"You don't have enough time to watch {movie}, you need {ceil(diff)} more minutes.")
else:
    print(f"You have enough time to watch {movie} and left with {ceil(diff)} minutes free time.")