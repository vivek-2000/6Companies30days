#Distributing M items in a circle of size N starting from K-th position
#https://www.geeksforgeeks.org/distributing-m-items-circle-size-n-starting-k-th-position/
n=int(input())
m=int(input())
k=int(input())
if m<(n-k+1):
    print(m+k-1)
m = m - (n - k + 1)
if(m % n == 0):
    print(n)
else:
    print(m % n)
