def is_armstrong(number):
    number_str = str(number)
    num_digits = len(number_str)
    total = 0
    for digit in number_str:
        total = total + int(digit) ** num_digits
        if total == number:
            return True
        else:
            return False


print(is_armstrong(153))  
print(is_armstrong(123))  
print(is_armstrong(9474)) 
