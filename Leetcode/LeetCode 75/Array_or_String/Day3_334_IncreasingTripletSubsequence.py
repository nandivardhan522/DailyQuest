class Solution:
    def increasingTriplet(self, nums):
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

sol=Solution()
nums = [1,2,3,4,5]
print(sol.increasingTriplet(nums))

'''
Time Complexity
    Iterating Through the Array: The loop runs through each element of the array exactly once. The time complexity for this part is O(n), where n is the number of elements in the input list nums.
    Overall Time Complexity: Since there's only one loop that runs through the array, the overall time complexity is
        O(n).
Space Complexity
The solution uses only two variables first and second in addition to the input array. Hence, the space complexity is 
O(1), which is constant space.
'''