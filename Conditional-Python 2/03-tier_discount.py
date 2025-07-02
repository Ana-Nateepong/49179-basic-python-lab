price = int(input())#recieve input
if(price >= 2000):#decide if the price is >= or not if yes 15 discount
    print(price - (price * 15/100))#(price * 15/100) is the find the discount
elif(price >= 1000):
    print(price - (price * 10/100))
elif(price > 500):
    print(price - (price * 5/100))
else:
    print(price)
    