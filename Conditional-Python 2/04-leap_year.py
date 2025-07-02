year = int(input())#recieve input
if(year%4 == 0 and year%100 != 0) or (year%400 == 0): #find does the input has remainder or not after /4 and if the input /100 is = 0 or not
    print("Leap year")                                  #and find that can it be divide by 400 without a remainder
else:
    print("Not a Leap year") 