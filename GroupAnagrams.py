from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d=defaultdict(list)
        for i in strs:
            a="".join(sorted(i))
            d[a].append(i)
        for k,v in d.items():
            ans.append(d[k])
        return ans
            