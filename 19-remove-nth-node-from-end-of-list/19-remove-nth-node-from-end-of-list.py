# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        x=[]
        
        while(head):
            
            x.append(head.val)
            head=head.next
        
        y=x[::-1]
        
        del y[n-1]
        
        y=y[::-1]
        
        cur=dummy=ListNode(0)
        
        for i in y:
            cur.next=ListNode(i)
            cur=cur.next
        
        return dummy.next
        
        
            
        