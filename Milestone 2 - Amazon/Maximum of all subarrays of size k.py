#User function Template for python3
#239. Sliding Window Maximum
from heapq import heappop,heappush
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        #code here
        ans=[]
        res=[]
        i=0
        j=0
        while j<n:
            if j-i+1<k:
                heappush(ans,(-arr[j],j))
            else:
                heappush(ans,(-arr[j],j))
                res.append(-ans[0][0])
                while len(ans) and ans[0][1]<=i:
                    heappop(ans)
                i+=1
            j+=1
                        
        return  res
