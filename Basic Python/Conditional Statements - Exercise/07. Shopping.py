

budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())


video_cards_off = 0.85
video_cards_price_per_unit = 250
processors_off = 0.35
ram_memory_off = 0.10
discount = 1

video_cards_total_sum = video_cards * video_cards_price_per_unit
processors_total_sum = (processors * video_cards_total_sum) * processors_off
ram_memory_total_sum = (ram_memory * video_cards_total_sum) * ram_memory_off

if video_cards > processors:
    discount = 0.85

total_sum_to_pay = budget - ((video_cards_total_sum + processors_total_sum + ram_memory_total_sum) * discount)


if total_sum_to_pay >= 0:
    print(f'You have {abs(total_sum_to_pay):.2f} leva left!')
else:
    print(f"Not enough money! You need {abs(total_sum_to_pay):.2f} leva more!")