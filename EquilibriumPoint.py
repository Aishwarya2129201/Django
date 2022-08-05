# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        total_sum = 0
        sum_so_far = 0
        if N == 0:
            return -1
        
        for i in range(0,N):
            total_sum += A[i]
            
        for i in range(0,N):
            total_sum -= A[i]
            if(total_sum == sum_so_far):
                return (i+1)
            sum_so_far += A[i]
            
        return -1
