import heapq
class Solution:
    def findKthLargest(self, nums, k):
        nums=[-n for n in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -nums[0]

nums = [3,2,1,5,6,4]
k = 2
sol=Solution()
print(sol.findKthLargest(nums,k))
'''
Time Complexity:
    Heapify the list: heapq.heapify(nums) transforms the list into a heap.
    Time complexity: O(n), where n is the number of elements in the list.
    Pop k−1 elements from the heap: heapq.heappop takes O(logn) time per operation.
    perform this operation k−1 times.
    Time complexity: O(klogn).
    Overall Complexity: O(n)+O(klogn)=O(n+klogn).
    For small k relative to n, the O(n) term dominates, making the solution very efficient.
Space Complexity
    We are not using any additional space apart from the input list and a few variables.
    Transforming nums into a heap is done in-place, so the space complexity is:
    Space complexity: O(1) (in-place heap).
'''