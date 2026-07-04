num=int(input("Enter a Number:"))
orignal=num
sum=0
count = len(str(num))
while num!=0:
    digit=num%10
    sum=sum+digit**count
    num=num//10

if sum==orignal:
    print("The Number is Armstrong Number")
else:
    print("The Number is not Armstrong Number")
    
    