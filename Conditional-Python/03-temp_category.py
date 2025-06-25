tem = int(input())
if(tem<=0):
    print("Freezing")
elif(tem>=1 and tem<=15):
    print("Cold")
elif(tem>=16 and tem<=30):
    print("Warm")
else:
    print("Hot")