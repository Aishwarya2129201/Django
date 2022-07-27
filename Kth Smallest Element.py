import heapq as hq

class Solution:
    def kthSmallest(self,arr, l, r, k):
        maxheap=[]
        for i in range(0,r+1):
            hq.heappush(maxheap,-arr[i])
            
            if len(maxheap) > k:
                hq.heappop(maxheap)
        
        return -maxheap[0]
