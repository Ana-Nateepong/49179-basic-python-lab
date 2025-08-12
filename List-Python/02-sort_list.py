n = int(input())#recieve input
numbers = []#create a list
for i in range(n):#recieve n and put it in a list
    num = int(input())
    numbers.append(num)
print("ลิสต์เดิม:", numbers)
numbers.sort()#Sort the list from least to greatest
print("ลิสต์เรียงแล้ว:", numbers)