# Учебната година вече е започнала и отговорничката на 10Б клас - Ани трябва да купи определен брой пакетчета с химикали,
# пакетчета с маркери, както и препарат за почистване на дъска. Тя е редовна клиентка на една книжарница,
# затова има намаление за нея, което представлява някакъв процент от общата сума. Напишете програма,
# която изчислява колко пари ще трябва да събере Ани, за да плати сметката, като имате предвид следния ценоразпис:
#     • Пакет химикали - 5.80 лв.
#     • Пакет маркери - 7.20 лв.
#     • Препарат - 1.20 лв (за литър)
# Вход
# От конзолата се четат 4 числа:
#     • Брой пакети химикали - цяло число в интервала [0...100]
#     • Брой пакети маркери - цяло число в интервала [0...100]
#     • Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#     • Процент намаление - цяло число в интервала [0...100]
# Изход
# Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.


pens_package_price = 5.80
materials_price = 7.20
cleaner = 1.20


pens = float(input())
materials = float(input())
board_cleaner_liters = float(input())
discount = float(input())

pens_price = pens * pens_package_price
materials_total_price = materials * materials_price
board_cleaner_price = board_cleaner_liters * cleaner
all_price = pens_price + materials_total_price + board_cleaner_price
total_price = all_price - (all_price * (discount / 100))

print(total_price)