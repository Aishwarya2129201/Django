import heapq as hq

class Solution:
    def kthLargest(self, arr, l, r, k):
        minheap = []
        for i in range(r+1):
            hq.heappush(minheap, arr[i])
            if len(minheap) > k:
                hq.heappop(minheap)

        return minheap
        
if __name__ == "__main__":
    size = int(input("Enter the number of elements: "))
    arr = list(map(int, input().strip().split()))
    k = int(input("Enter the value of K:"))
    ob = Solution()
    print(ob.kthLargest(arr, 0, size-1, k))
