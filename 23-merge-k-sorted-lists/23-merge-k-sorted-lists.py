# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        x=[]
        head=point=ListNode(0)
        
        for i in lists:
            
            while(i):
                x.append(i.val)
                i=i.next
        
        x.sort()
        print(x)
        
        cur=dummy=ListNode(0)
        
        for i in x:
                
                cur.next=ListNode(i)
                cur=cur.next
        
        return dummy.next
                
        
        
            
            
        