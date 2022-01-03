#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        ans=""
        st=[]
        for i in range(len(S)+1):
            st.append(i+1)
            if i==len(S) or S[i]=="I":
                while len(st):
                    ans+=str(st.pop())
        return ans
