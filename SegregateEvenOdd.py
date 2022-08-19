class Solution:

	def segregateEvenOdd(self,arr, n):
	    even = []
        odd = []
        for i in arr:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
                
        even.sort()
        
        
        for i in sorted(odd):
            even.append(i)
            
        for i in range(n):
            arr[i] = even[i]
        
        return arr
