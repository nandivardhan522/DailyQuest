class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        def distinct(string):
            l = set(string)
            return len(l)

        left = 0
        right = len(s) - 1
        d = {}
        visited = set()
        while (left < len(s) - 2):
            if (s[left] not in visited):
                while (right > left + 1):
                    if s[left] == s[right]:
                        d[(left, right)] = s[left + 1:right]
                        break
                    else:
                        right -= 1
                visited.add(s[left])
            right = len(s) - 1
            left += 1
        l = list(d.values())
        res = 0
        for i in l:
            res += distinct(i)
        return res
Solution = Solution()
s = "aabca"
print(Solution.countPalindromicSubsequence(s))