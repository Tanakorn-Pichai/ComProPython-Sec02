total = 0.0
with open('sales.txt' , 'r') as sales_file:
    line = sales_file.readline()

    while line != '':
        amount = float(line)
        total += amount
        print(format(amount,'.2f'))
        line =sales_file.readline()
    print(format(total,'.2f'))