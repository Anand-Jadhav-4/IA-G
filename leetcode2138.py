"""
2138. Divide a String Into Groups of Size k

Easy

A string s can be partitioned into groups of size k using the following procedure:
The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each element can be a part of exactly one group.
For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

Given the stri

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters only.
- 1 <= k <= 100
- fill is a lowercase English letter.
"""

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # Append fill characters until length of s is divisible by k
        while len(s) % k:
            s += fill
        
        ans = []
        # Create groups of size k
        for i in range(0, len(s), k):
            ans.append(s[i:i+k])
        return ans

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.divideString("abcdefghi", 3, "x"))  # Output: ["abc", "def", "ghi"]
    print(sol.divideString("abcdefghij", 3, "x")) # Output: ["abc", "def", "ghi", "jxx"]
