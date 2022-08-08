size = int(input("Enter the number of elements:"))
arr = []
for i in range(size):
    element = int(input("Enter the element:"))
    arr.append(element)
low = 0
high = size-1
if size % 2 == 0:
    mid1 = size // 2
    mid2 = size // 2 + 1
    while low <= mid1 and high >= mid2:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
else:
    mid = size // 2
    while low <= mid:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    
print(arr)
