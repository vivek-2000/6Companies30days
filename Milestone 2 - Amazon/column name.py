#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        res=""
        while n:
            res=chr((n-1)%26+ord('A'))+res
            n=(n-1)//26
        return res
            