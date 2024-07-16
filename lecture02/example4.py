man = int(input("Enter the number of man students: "))
woman = int(input("Enter the number of woman students: "))

sum = man + woman


print('man students:', format((man/sum)*100, '25.2f'),'%')
print('woman students:', format((woman/sum)*100, '25.2f','%'))