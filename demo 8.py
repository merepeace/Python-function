#Variable-Length / Arbitary argument in python(*args)

def demo(*sports):
    print("Displaying passed arguments")

    for name in sports:
        print(name)

user_input=input("enter sports namer seperated by commas:")
sports_list=user_input.split(",")
#call
demo(*sports_list)
