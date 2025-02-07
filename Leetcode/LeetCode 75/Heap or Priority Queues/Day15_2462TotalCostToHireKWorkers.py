from heapq import heapify,heappush,heappop
class Solution:
    def totalCost(self, costs, k, candidates):
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapify(head_workers)
        heapify(tail_workers)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heappop(head_workers)
                if next_head <= next_tail:
                    heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                answer += heappop(tail_workers)
                if next_head <= next_tail:
                    heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return answer

costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

Solution = Solution()
print(Solution.totalCost(costs,k,candidates))

'''
Time Complexity Analysis:
    Overall Complexity:
    O(candidates log candidates + k log candidates) ≈ O((candidates + k) log candidates)
    In the worst case, candidates ≈ n, so complexity simplifies to O(n log n).
Space Complexity
    O(candidates) for head_workers heap.
    O(candidates) for tail_workers heap.
    O(1) for extra variables.
    Total: O(candidates).
'''