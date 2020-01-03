
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def add(self,x):
        temp = self
        newNode = ListNode(x)
        while(temp.next):
            temp = temp.next
        
        temp.next = newNode
    
    def printNode(self):
        temp = self
        while(temp):
            print(temp.val)
            temp = temp.next
        


class Solution:
    def addTwoNumbers(self, l1: ListNode,l2 : ListNode):
        carry =0
        temp: ListNode = None
        result: ListNode = None
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
    

l1 = ListNode(2)
l1.add(4)
l1.add(3)

l2 = ListNode(5)
l2.add(6)
l2.add(4)

result = Solution()
output: ListNode = result.addTwoNumbers(l1,l2)
output.printNode()
