#User function Template for python3
class Solution:

	def matchPairs(self,nuts, bolts, n):
		# code here
		o = ['!', '#', '$', '%', '&', '*', '@', '^', '~']
		ans=[]
		for i in nuts:
		    ans.append(i)
        nuts.clear()
		bolts.clear()
		
		for i in o:
		    if i in ans:
		        
		        nuts.append(i)
		        bolts.append(i)
