class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        a = [None]*len(arr)
        i = 0
        for j in range (0,n):
            if arr[j] >= 0:
                a[i] = arr[j]
                i += 1
        for j in range (0,n):
            if arr[j] < 0:
                a[i] = arr[j]
                i += 1
                
        for j in range (0,n):
            arr[j] = a[j]
