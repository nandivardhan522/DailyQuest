class Solution:
    def countBits(self, n: int):
        return [i.bit_count() for i in range(0, n + 1)]

n=5
Solution = Solution()
print(Solution.countBits(n))

'''
Time and Space Complexity
Time Complexity:
O(n) since we iterate over numbers from 0 to n, applying bit_count() on each.
bit_count() runs in O(1) (hardware-optimized for integers), so the loop dominates.
Space Complexity:
O(n) since we store the result in a list of length n+1.
'''