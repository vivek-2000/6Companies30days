class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod=1
        count=0
        if k==0:
            return 0
        i=0
        for j in range(len(nums)):
            prod*=nums[j]
            while i<=j and prod>=k:
                prod//=nums[i]
                i+=1
                
            count+=(j-i+1)
        return count