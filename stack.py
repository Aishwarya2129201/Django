stack = []
def getChoice():
    print("\nMenu Details: \n1-PUSH \n2-POP \n3-DISPLAY \n4-EXIT")
    ch = int(input("Enter the choice: "))
    return ch

def pushitem(item):
    stack.append(item)
    
def popitem():
    item = stack[-1]
    del stack[-1]
    return item

def display():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    
#Main function starts here
choice = getChoice()
while choice!=4:
    if choice == 1:
        item = int(input("Enter the element: "))
        pushitem(item)
    elif choice == 2:
        if(len(stack)!=0):
            item = popitem()
            print("Popped value is ",item)
        else: 
            print("Stack underflow")
    elif choice == 3:
        if(len(stack)!=0):
            display()
        else: 
            print("Stack underflow")
    else:
        print("Wrong choice")
    choice = getChoice()
print("Stack operations are over.")