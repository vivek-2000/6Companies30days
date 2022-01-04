#User function Template for python3

class Solution:
    def squaresInChessBoard(self, N):
         # code here
         n=N
         return ((n*(n+1)//2)*(((2*n)+1))//3)