class Solution:
    def findDifference(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

sol=Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
print(sol.findDifference(nums1,nums2))
'''
Time Complexity:
    Creating sets: O(n1+n2).
    Set difference operations: O(n1+n2).
    Overall Time Complexity: O(n1+n2).
Space Complexity:
    Only two sets (set1 and set2) are used, reducing space usage compared to the original code.
    Overall Space Complexity: O(n1+n2).
'''