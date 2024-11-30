

deposit = int(input())
deposit_time = int(input())
annual_interest = float(input())

annual_interest_sum = (deposit * (annual_interest / 100))
annual_interest_monthly = (annual_interest_sum / 12)
total_deposit = (deposit + (deposit_time * annual_interest_monthly))

print(total_deposit)