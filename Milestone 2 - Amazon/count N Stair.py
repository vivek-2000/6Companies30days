class Solution:
    
    #Function to count number of ways to reach the nth stair 
    #when order does not matter.
    def countWays(self,m):
        
        mod = 1000000007
        # code here
        return m//2+1