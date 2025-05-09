#average
a,b=map(int,input("Enter any two numbers").split())
def avg(a,b):
    s=a+b
    av=s/2
    return av

result=avg(a,b)
print(f"The average of {a} and {b} is {result}")