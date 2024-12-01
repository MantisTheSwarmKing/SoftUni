import re

# Input data
participants = input().split(", ")
racers = {participant: 0 for participant in participants}

while True:
    data = input()
    if data == "end of race":
        break

    # Extract name (letters only) and distance (sum of digits)
    name = ''.join(re.findall(r'[A-Za-z]', data))
    distance = sum(map(int, re.findall(r'\d', data)))

    # Update distance for valid racers
    if name in racers:
        racers[name] += distance

# Sort racers by distance in descending order
sorted_racers = sorted(racers.items(), key=lambda x: x[1], reverse=True)

# Output top 3 racers
places = ["1st", "2nd", "3rd"]
for i in range(min(3, len(sorted_racers))):
    print(f"{places[i]} place: {sorted_racers[i][0]}")