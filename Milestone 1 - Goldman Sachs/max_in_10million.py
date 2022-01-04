from heapq import heapify,heappush,heappop
arr=[1,2,3,4,5,6,7,8,9,10,11,55,77,99,66,100,556,8888,29854,54345,524,7777,2457,3216,876]
heap=[]
for i in arr:
    heappush(heap,i)
    if len(heap)>10:
        heappop(heap)
print(heap)
