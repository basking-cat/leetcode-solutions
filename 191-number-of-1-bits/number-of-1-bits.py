class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n-1 # remove the rightmost 1
            res += 1
        return res

        # time: O(1)
        # space: O(1)