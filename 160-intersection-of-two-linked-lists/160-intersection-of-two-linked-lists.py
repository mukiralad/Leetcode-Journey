# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        d1=headA
        d2=headB
        
        l1=0
        l2=0
        
        while(d1):
            l1+=1
            d1=d1.next
        
        while(d2):
            l2+=1
            d2=d2.next
            
        
        dif=abs(l1-l2)
        
        if(l1>l2):
            large=headA
            small=headB
        else:
            large=headB
            small=headA
        
        for i in range(dif):
            large=large.next
            
        while(large and small):
            if(large==small):
                return large
            large=large.next
            small=small.next
            
        return None
        
        
        
            
            
        