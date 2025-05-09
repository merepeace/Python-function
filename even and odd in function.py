# even odd

def evenandodd(a):
    if(a%2==0):
        return 1
    elif(a%2!=0):
        return -1
    else:
        return 0
n=int(input("Enter a number:"))

result=evenandodd(n)

if result==1:
    print(f"Entered number {n} is even")
elif result==-1:
    print(f"Entered number {n} is odd")
else:
    print(f"Entered number {n} is zero  ")