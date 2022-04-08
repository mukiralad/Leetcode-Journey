# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=head
        length=0
        while(temp):
            length=length+1
            temp=temp.next
        
        curr=head
        
        for i in range(length//2):
            curr=curr.next
        
        return(curr)
        
            
    
       
            
        