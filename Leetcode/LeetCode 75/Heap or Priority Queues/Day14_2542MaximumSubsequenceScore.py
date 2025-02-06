import heapq
class Solution:
    def maxScore(self, nums1, nums2, k: int) -> int:
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: -x[1])
        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)
        answer = top_k_sum * pairs[k - 1][1]
        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])
            answer = max(answer, top_k_sum * pairs[i][1])

        return answer

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3

Solution = Solution()

print(Solution.maxScore(nums1,nums2,k))

'''
Analysis:
Time Complexity:
    Overall Complexity:
    O(n log n + (n-k) log k) approximately O(n log n) (since sorting dominates for large n).
    
Space Complexity:
    O(n) for storing the pairs list.
    O(k) for the min-heap (top_k_heap).
    Total: O(n).
    
    
'''