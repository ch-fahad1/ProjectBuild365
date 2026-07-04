num=int(input("Enter a Number: "))
sum=0
while(num != 0):
    sum=sum+(num%10)
    num=num//10

print("Total sum of a number digits are: ",sum)