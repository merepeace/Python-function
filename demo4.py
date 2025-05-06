#keyword argument
def details(name,rank ,points):
    print("\nStudent Name =",name)
    print("Student  Rank =",rank)
    print("Student Points =",points)

    #call
details(rank=5, name="Jack" , points=12)
details(rank=1 , points=150.5 , name="John")