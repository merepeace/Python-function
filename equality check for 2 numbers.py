#program to check two numbers are equal or not
a=int(input("Enter firt number: "))
b=int(input("Enter second number: "))

def check(a, b):
    if (a == b):
        return 0
    elif (a > b):
        return 1
    else:
        return -1

result = check(a,b)
if(result==0):
    print(f"The number  {a} is equal to{b}.  ")
elif(result==1):
    print(f"The number  {a} is greater than to {b}.  ")
else:
    print(f"The number {a} is Less than {b}.  ")
