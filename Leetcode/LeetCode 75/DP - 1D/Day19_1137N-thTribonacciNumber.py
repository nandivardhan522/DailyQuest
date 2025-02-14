class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1

        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t2
Solution = Solution()
n=4
print(Solution.tribonacci(n))

'''
Time Complexity:
O(n)
The loop iterates from 3 to n, which is n-2 iterations. 
In each iteration, only constant time work is done (updating three variables). 
Hence, the time complexity is linear in terms of n.
Space Complexity:
O(1)
The space complexity is constant because you are only using three variables (t0, t1, t2) to store the intermediate values. 
'''