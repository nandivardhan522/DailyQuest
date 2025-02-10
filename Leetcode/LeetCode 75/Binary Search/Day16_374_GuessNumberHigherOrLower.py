def guess(num):
    return
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = (left + right) // 2
        while (left <= right):
            if (guess(mid) == -1):
                right = mid - 1
                mid = (left + right) // 2
            elif (guess(mid) == 1):
                left = mid + 1
                mid = (left + right) // 2
            elif (guess(mid) == 0):
                return mid

'''
Time Complexity Analysis
The binary search algorithm reduces the search space by half in each step, making it very efficient.
Worst-case scenario: The search space is reduced from n to n/2, then n/4, then n/8, and so on.
This gives a time complexity of:O(logn)

Space Complexity Analysis
The algorithm only uses a few integer variables (left, right, mid), making the space complexity O(1) (constant space).
'''