class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return answer

temperatures = [73,74,75,71,69,72,76,73]
Solution = Solution()
print(Solution.dailyTemperatures(temperatures))

'''
Time Complexity:
O(n) — Each index is pushed and popped from the stack at most once, where 
n is the length of the temperatures list. Therefore, the overall time complexity is linear.
Space Complexity:
O(n) — Due to the space used by the stack and answer list, both of which can store up to 
n elements in the worst case.
'''