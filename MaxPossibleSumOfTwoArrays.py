class Solution:

    def MaxSum(self, A, B, N):
        A.sort()
        B.sort()
        
        sumValue = 0
        
        for i in range(N):
            sumValue += A[i]*B[i]
            
        return sumValue

