num = int(input())  #recieve input
result = 0
for i in range(1, num + 1):
    if i % 2 != 0:  #find odd number
        result += i  #add the odd number
print(result)  #print the result
