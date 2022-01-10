#User function Template for python3

from collections import deque,defaultdict
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		
		dll=deque()
		mapp=defaultdict(int)
		res=""
		for i in range(len(A)):
		    mapp[A[i]]+=1
		    if mapp[A[i]]==1:
		        dll.append(A[i])
		    while len(dll) and mapp[dll[0]]>1:
		        dll.popleft()
		    if len(dll)==0:
		        res+="#"
		    else:
		        res+=dll[0]
	    return res
		    