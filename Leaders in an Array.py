class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        Arr = []
        max = A[N-1]
        
        for i in range(N-1, -1, -1):
            if A[i] >= max:
                Arr.append(A[i])
                max = A[i]
                
        res = Arr[::-1]
        return res
