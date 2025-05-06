#Variable-Length / Arbitary argument in python(*args)

def demo(*sports):
    print("Displaying passed arguments")

    for name in sports:
        print(name)

#call
demo("Football","Hockey","Cricket","Chess","Batminton")
