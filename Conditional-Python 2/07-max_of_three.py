num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num1 >= num2) and (num1 >= num3):#if num1 is greater than num2 and num3 print num1
    print(num1)
elif (num2 >= num1) and (num2 >= num3):#if num2 is greater than num1 and num3 print num2
    print(num2)
else:
    print(num3)