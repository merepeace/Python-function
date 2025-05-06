#Variable-Length / Arbitary argument in python(*args)

def demo(*sports):
    print("Sports 1=",sports[0])
    print("Sports 2=",sports[1])
    print("Sports 3=",sports[2])
    print("Sports 4=",sports[3])
    print("Sports 5=",sports[4])

#call
demo("Football","Hockey","Cricket","Chess","Batminton")
