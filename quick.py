
def Quicksort(list, start, end):
    if start<end:
        position = partition(list, start, end)
        Quicksort(list, start, position-1)
        Quicksort(list, position+1, end)
        
def partition(list, start, end):
    i = start-1
    pivot = list[end]
    for j in range(start,end):
        if list[j] <= pivot:
            i+=1
            list[i],list[j] = list[j],list[i]
    list[i+1], list[end] = list[end], list[i+1]
    return i+1

def printList(list):
    for i in range(len(list)):
        print(list[i])
    
list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter the element: "))
    list.append(element)

print("Before Sorting: ")
printList(list)
print("After Sorting: ")
Quicksort(list,0,n-1)
printList(list)