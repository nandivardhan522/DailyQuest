class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []

        def backtrack(start, temp):
            if len(temp) == k:
                if sum(temp) == n:
                    res.append(temp.copy())
                return

            for j in range(start, 10):
                temp.append(j)
                backtrack(j + 1, temp)
                temp.pop()

        backtrack(1, [])
        return res

k = 3
n = 7

Solution = Solution()
print(Solution.combinationSum3(k,n))