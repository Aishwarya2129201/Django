class Solution:
    def majorityElement(self, A, N):
        #Your code here
        count = 1
        res = 0
        for i in range(N):
            if A[res] == A[i]:
                count += 1
                
            else:
                count -= 1
                
            if count == 0:
                count = 1
                res = i
            
        count = 0
        for i in range(N):
            if A[res] == A[i]:
                count += 1
                
        if count <= N//2:
            return -1
        
        else:
            return A[res]
            
        return -1
