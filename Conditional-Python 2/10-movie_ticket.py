age = int(input())
day = int(input()) 
if (age < 13): #check if age less than 13 or not if yes price 100
    price = 100
elif (age <= 60):#check if age is less than or equal to 60 if yes price 108
    price = 180
else: 
    price = 120
if day == 6 or day == 7: #add 50 if it day 6 or 7 which is the weekend
    price += 50
print(price)
