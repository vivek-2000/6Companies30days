#Your task is to complete this function
#Function should return complete string
from collections import OrderedDict
def encode(arr):
    # Code here
    s=""
    ans=""
    count=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            ans+=arr[i-1]+str(count)
            count=1
    ans+=(arr[-1]+str(count))
    
            
    return ans
        