from heapq import heappop,heappush
class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
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
                