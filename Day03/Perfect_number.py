num=int(input("Enter a Number: "))
sum=0
for i in range(1,num):
    if num % i==0:
        sum=sum+i

if sum==num:
    print("The number is Perfect Number")
else:
    print("Not a perfect Number")
