import re


def process_sales(data):
    valid_sales = []
    total_income = 0.0

    for line in data.splitlines():
        if line == "end of shift":
            break

        match = re.match(r'%(\w+)%<(\w+)>(\d+|\|)(\d+(\.\d{1,2})?)\$', line)
        if match:
            name, product, count, price = match.groups()
            if count == '|':
                count = 1
            else:
                count = int(count)
            price = float(price)
            total = count * price
            valid_sales.append((name, product, total))
            total_income += total

    for name, product, total in valid_sales:
        print(f"Valid: {name} - {total:.2f}")
    print(f"Total income: {total_income:.2f}")


data = """%InvalidName%<Croissant>|2|10.3$
%Peter%<Gum>1.3$
%Maria%<Cola>|1|2.4
%Valid%<Valid>valid|10|valid20$
end of shift"""

process_sales(data)
