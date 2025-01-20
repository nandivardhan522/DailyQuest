class Solution:
    def maxArea(self, height):
        i=0
        j=len(height)-1
        area=float('-inf')
        while(i<j):
            area=max(area,min(height[i],height[j])*(j-i))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return area

sol=Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))
'''
Complexity Analysis:
    Time Complexity:
        The algorithm uses a two-pointer approach and traverses the list only once. 
        Thus, the time complexity is: O(n).
    Space Complexity:
        The algorithm uses a constant amount of space for variables (i, j, area), 
        making the space complexity: O(1)
'''