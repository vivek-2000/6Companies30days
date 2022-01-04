class Solution:
    def fun(s,idx,n,t):
        if idx>=n:
            return 1
        if t[idx]!=-1:
            return t[idx]
        if s[idx]=='0':
            return 0
        x=Solution.fun(s,idx+1,n,t)
        y=0
        if (idx<n-1 and (s[idx]=='1' or (s[idx]=='2'and s[idx+1]<'7'))):
            y=Solution.fun(s,idx+2,n,t)
        t[idx]=x+y
        return t[idx]
    def numDecodings(self, s: str) -> int:
        n=len(s)
        t=[-1]*101
        return Solution.fun(s,0,n,t)