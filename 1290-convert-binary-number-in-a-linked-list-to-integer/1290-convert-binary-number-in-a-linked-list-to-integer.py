# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        temp=head
        x=""
        
        while(temp):
            x+=str(temp.val)
            temp=temp.next
        
        
        x=int(x,2)
        return x
        
        
        
        
            
        