num=int(input("Enter a Number: "))
count=0
while(num != 0):
    num=num//10
    count+=1

print("Total digits in a number are: ",count)