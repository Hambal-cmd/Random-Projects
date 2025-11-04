# to find the largest number from a list of number entered by the user
def largest(): 
    a=[]
    n=int(input("Enter the nubmer of elements required: "))
    largest=None

    for i in range(n):
        a.append(int(input(f"Enter element {i+1}: ")))

    for var in a:
        if largest==None or var>largest:
            largest=var

    print("The Largest is: ",largest)

def isprime(num):
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=1
    if count==1:
        return True

def SumPrime():
    num = int(input("Enter the number till whose sum of prime has to be found: "))
    prime = []
    while num>0:
        if isprime(num):
            prime.append(num)
        num-=1
    
    sum=0
    for i in prime:
        sum = sum+i
    
    print("Sum: ",sum)

SumPrime()

