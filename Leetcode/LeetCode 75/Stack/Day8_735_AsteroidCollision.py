class Solution:
    def asteroidCollision(self, asteroids):
        stk = []

        for i in asteroids:
            while stk and i < 0 < stk[-1]:
                if stk[-1] < -i:
                    stk.pop()
                    continue
                elif stk[-1] == -i:
                    stk.pop()
                break
            else:
                stk.append(i)
        return stk
sol=Solution()
asteroids = [5,10,-5]
print(sol.asteroidCollision(asteroids))

'''
Time Complexity:
    Processing Each Asteroid:
        Each asteroid is processed once, either being pushed to or popped from the stack. 
        The stk.pop() and stk.append() operations are O(1).
    Overall Complexity:
        Since each asteroid is processed once, 
        the overall time complexity is O(n), where n is the number of asteroids.
Space Complexity:
The stack stores at most all the asteroids if there are no collisions.
Space complexity is O(n) in the worst case.
'''