import heapq as hq

def nearlySorted(arr, k):
    minheap = []
    sArray = []
    for i in range(len(arr)):
        hq.heappush(minheap,arr[i])
        if len(minheap)>k:
            sArray.append(minheap[0])
            hq.heappop(minheap)
    while(len(minheap)>0):
        sArray.append(minheap[0])
        hq.heappop(minheap)
