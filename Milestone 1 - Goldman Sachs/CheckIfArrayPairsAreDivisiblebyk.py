from collections import defaultdict
class Solution:
    def canArrange(self, arr, k: int) -> bool:
        dct=defaultdict(int)
        count=0
        for i in arr:
            dct[i%k]+=1
        if dct[0]%2==1:
            return False
        
        for i in range(1,k):
            if dct[i]!=dct[k-i]:
                return False
            count+=dct[i]
        print(count+dct[0]//2)
        print(len(arr)//2)
        if (count+(dct[0]//2))>=len(arr)//2:
            return True
        else:
            return False
            
        