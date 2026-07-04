num=int(input("Enter a Number: "))

if num<=1:
    print("Not Prime:")
    exit()

for i in range(2,num):
    if num%i==0:
        print("Not a prime number cause",num ,"%",i,"= 0")
        exit()
else:
    print("prime number")