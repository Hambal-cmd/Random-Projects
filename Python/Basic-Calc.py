a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("Enter 1-addition 2-subtraction 3-mutiplication 4-division")
n=int(input("Enter the choice:"))

if(n==1):
    print(a+b)
if(n==2):
    print(a-b)
if(n==3):
    print(a*b)
if(n==4):
    print(a/b)
else:
    print("Invalid choice")
