
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

123 % 10 = 3
12 % 10 = 2
1 % 10 = 1

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
 For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows
"""

class solution:
    def reverse(self,x:int) -> int:
        print(self.modnumber(x))

    def modnumber(self,x:int):
        flag = 0
        if x < 0:
            flag = 1
            x = -(x)
        count =0
        out = 0
        while(x > 0):
            out = out * 10 + (x % 10)
            # count += 1
            x = x // 10
        if abs(out) > pow(2, 31) - 1: return 0
        elif (flag == 0): return out
        else: return -out

    # def stringNumber(self,x:int):


solve = solution()
solve.reverse(1534236469)
solve.reverse(-123)
solve.reverse(102001)