
volume_pool_liters = int(input())
volume_water_liter_per_hour_pipe1 = int(input())
volume_water_liter_per_hour_pipe2 = int(input())
hours_worker_not_present = float(input())

water_use_pipe1 = volume_water_liter_per_hour_pipe1 * hours_worker_not_present
water_use_pipe2 = volume_water_liter_per_hour_pipe2 * hours_worker_not_present

water_use = water_use_pipe2 + water_use_pipe1

if water_use <= volume_pool_liters:
    print(f'The pool is {water_use / volume_pool_liters:.2%} full. Pipe 1: {water_use_pipe1 / water_use:.2%}. Pipe 2: {water_use_pipe2 / water_use:.2%}.')
else:
    print(f'For {hours_worker_not_present:.2f} hours the pool overflows with {water_use - volume_pool_liters:.2f} liters.')