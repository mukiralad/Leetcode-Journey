# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        temp=head
        
        x=[]
        
        while(temp):
            x.append(temp.val)
            temp=temp.next
        
        d=""
        
        for i in x:
            d+=str(i)
        print(d)
        
        
        
        res=int(d,2)
        
        return res
            
            
            
        