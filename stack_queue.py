def stack_queue():
    list1=[]
    while True:
        print("1.stack method")
        print("2.queue method")
        print("3.exit")
        opt=int(input("enter your option"))
        match(opt):
            case 1:
                stack_method(list1)
            case 2:
                queue_method(list1)
            case 3:
                print("bye bye visit again")
                break
            case _:
                print("please enter valid option")
def stack_method(list1):
    while True:
        print("1.push")
        print("2.pop")
        print("3.display")
        print("4.exit")
        op=int(input("enter option for what do yuo want"))
        match(op):
            case 1:
                list1.append(int(input("enter value")))
                print("value entered queue sucessfully")
            case 2:
                if len(list1)==0:
                    print("it's empty list")
                else:
                    list1.pop()
                    print("value delete sucessffully")
            case 3:
                print(list1)
            case 4:
                break
            case _:
                print("please enter a valid number")
def queue_method(list1):
    while True:
        print("1.push")
        print("2.pop")
        print("3.display")
        print("4.exit")
        op=int(input("enter option for what do yuo want"))
        match(op):
            case 1:
                list1.append(int(input("enter value")))
                print("value entered queue sucessfully")
            case 2:
                if len(list1)==0:
                    print("it's empty list")
                else:
                    del list1[0]
                    print("value delete sucessffully")
            case 3:
                print(list1)
            case 4:
                break
            case _:
                print("please enter a valid number")
stack_queue()
