total = 0.0
with open('sales.txt' , 'r') as sales_file:
    for line in sales_file:
        amount = float(line.strip())
        total += amount
        print(format(amount,'.2f'))
    print(format(total,'.2f'))