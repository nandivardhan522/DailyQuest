class Solution:
    def letterCombinations(self, digits: str):
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]

        if(digits ==""):
            return []
        def backtrack(i,curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for c in d[digits[i]]:
                backtrack(i+1,curr + c)

        backtrack(0,"")
        return res

Solution = Solution()
digits="23"
print(Solution.letterCombinations(digits))

'''
Time Complexity:
The time complexity is O(4^n), where n is the length of digits.
This is because each digit can map to at most 4 letters (e.g., '7' and '9' have 4 letters each), and all combinations are explored.
Space Complexity:
The space complexity is O(n) for the recursion stack, plus O(4^n) for storing the results.
'''