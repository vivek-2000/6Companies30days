class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglynums=[1]
        i1=i2=i3=0
        while len(uglynums)<n:
            minnum=min(2*uglynums[i1],3*uglynums[i2],5*uglynums[i3])
            if minnum==2*uglynums[i1]:
                i1+=1
            if minnum==3*uglynums[i2]:
                i2+=1
            if minnum==5*uglynums[i3]:
                i3+=1
            uglynums.append(minnum)
        return uglynums[-1]
                
        