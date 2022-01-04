#space O(n)
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        ans=[]
        a=[0]*(n+1)
        for i in range(0,n):
            a[arr[i]]+=1
        for i in range(1,n+1):
            if a[i]>1:
                ans.append(i)
                break
        for i in range(1,n+1):
            if a[i]==0:
                ans.append(i)
                break
        return ans