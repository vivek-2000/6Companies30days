# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def skipMdeleteN(self, head, m, n):
        # Code here
        c=head
        prev=None
        while c:
            for i in range(m):
                if c==None:
                    break
                prev=c
                c=c.next
            for i in range(n):
                if c==None:
                    break
                c=c.next
            
            prev.next=c
        return head