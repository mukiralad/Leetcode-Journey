# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        nums1=[]
        nums2=[]
        
        temp1=l1
        
        temp2=l2
        
        while temp1 is not None:
            nums1.append(temp1.val)
            temp1=temp1.next
        
        while temp2 is not None:
            nums2.append(temp2.val)
            temp2=temp2.next
        
        
        x=nums1[::-1]
        y=nums2[::-1]
        
        one=""
        for i in x:
            one+=str(i)
        two=""
        for j in y:
            two+=str(j)
        
        ans=int(one)+int(two)
        
        ans=str(ans)
        ans=ans[::-1]
        
        curr=dummy=ListNode(0)
        
        for i in ans:
            curr.next=ListNode(i)
            curr=curr.next
        
        return dummy.next