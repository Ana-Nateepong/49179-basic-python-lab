n = int(input())#recieve input
numbers = []#create a list
even_numbers = []
odd_numbers = []
for i in range(n):#put input into a list
    num = int(input())
    numbers.append(num)
for num in numbers:#seperate even and odd number
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("เลขคู่:", even_numbers)
print("เลขคี่:", odd_numbers)