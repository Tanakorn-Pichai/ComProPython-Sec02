hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly pay rate: "))
if hours > 40 :
    hours_over = (hours-40)* (rate*1.5)
    pay = (40 * rate) + hours_over
    print ("The gross pay is $",pay)
else :
    pay = (hours * rate)
    print ("The gross pay is $",pay)