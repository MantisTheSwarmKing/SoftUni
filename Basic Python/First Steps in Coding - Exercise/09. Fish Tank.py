

length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

aquarium_size = length * width * height
aquarium_liters = float(aquarium_size * (1/1000))
water_volume = float(percentage / 100)
water_needed = aquarium_liters * (1 - water_volume)

print(water_needed)