num=int(input("Enter a number: "))
orignal=num
reversed=0
while(num != 0):
    digit=num%10
    reversed=reversed*10+digit
    num=num//10

if reversed==orignal:
    print("The Number is a Palindrome: ")
else:
    print("Number is Not a pailndrome")

    
