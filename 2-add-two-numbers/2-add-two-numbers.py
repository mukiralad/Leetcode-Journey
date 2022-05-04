# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1=l1
        
        res1=[]
        
        while(temp1):
            res1.append(temp1.val)
            temp1=temp1.next
        
        temp2=l2
        
        res2=[]
        
        while(temp2):
            res2.append(temp2.val)
            temp2=temp2.next
        
        num1=res1[::-1]
        num2=res2[::-1]
        
        ans1=int("".join(map(str,num1)))
        ans2=int("".join(map(str,num2)))
        
        final=ans1+ans2
        
        x=str(final)
        
        x=x[::-1]
        
        listt=[]
        
        for i in range(len(x)):
            listt.append(int(x[i]))
        
        
        curr=dummy=ListNode(0)
        
        for i in listt:
            curr.next=ListNode(i)
            curr=curr.next
        
        return dummy.next
        
        
        
        
        