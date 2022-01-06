class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        i=0
        minn=float('inf')
        n=len(nums)
        summ=0
        j=0
        while j<n:
            summ+=nums[j]
            while i<n and summ>=target:
                minn=min(minn,j-i+1)
                summ-=nums[i]
                i+=1
            j+=1
        if minn==float('inf'):
            return 0
            
        return minn
                
            
        