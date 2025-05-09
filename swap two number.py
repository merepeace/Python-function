
# swapping using function in Python

#a=int(input("Enter any frist number"))
#b=int(input("Enter any second number"))
a,b=map(int,input("Enter value of any two number After first number give space ").split())#Only for two digit number work here.
print(f"Before swapping:   {a}\t\t{b}")

def swap(a,b):
        a,b= b,a #swapping a,b
        return a,b # return swapped value

a,b=swap(a,b)
print(f"After swapping:    {a}\t\t{b}")
