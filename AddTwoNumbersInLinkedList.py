
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode,l2 : ListNode):
        carry =0
        temp = None
        result = None
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry,sum = divmod(val1+val2+carry,10)
            out = ListNode(sum)
            if result is None: #check if head is none
                result = out
            temp = result #point to head
        else:        
            temp.next = out
            temp = temp.next         
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
        return result
        
