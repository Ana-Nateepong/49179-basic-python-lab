n = int(input())#recieve input
numbers = []#create a list
for i in range(n):#recieve n and put it in a list
    num = int(input())
    numbers.append(num)
total = sum(numbers)#find the sum of the list
print("ผลรวม:", total)