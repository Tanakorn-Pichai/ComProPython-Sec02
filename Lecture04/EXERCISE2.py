input_columns = int(input("How many columns? "))

for i in range(1,101):  
    print(i,end=' ')  
    if i % input_columns == 0 :
        print()
    