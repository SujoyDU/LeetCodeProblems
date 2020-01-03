'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def longestSubStrWithoutRepeat(self, s:str) -> int:
        dictStr = {}
        start = 0
        count = 0
        maxCount = 0
        if not s: return 0
        for indx, ch in enumerate(s):
            if ch not in dictStr:
                dictStr[ch] = indx
                count += 1
            elif ch in dictStr:
                if dictStr[ch] >= start: 
                    maxCount = count if count > maxCount else maxCount
                    start = dictStr[ch]+1
                    count = indx - dictStr[ch]
                    dictStr[ch] = indx
                else: 
                    dictStr[ch] = indx
                    count += 1

        count = len(s) - start
        maxCount = count if count > maxCount else maxCount
        return maxCount


inputStr = "abcabcbb"
result = Solution()
print(result.longestSubStrWithoutRepeat(inputStr))