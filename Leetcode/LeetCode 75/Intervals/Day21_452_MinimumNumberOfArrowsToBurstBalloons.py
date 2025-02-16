class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])

        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        return arrows

points = [[10,16],[2,8],[1,6],[7,12]]
Solution = Solution()

print(Solution.findMinArrowShots(points))

'''
Time Complexity:
Sorting: O(NlogN), where N is the number of balloons.
Iteration: O(N) for going through each balloon.
Overall: O(NlogN) due to the sorting step.

Space Complexity:
O(1) (ignoring input storage) because only a few variables are used.

'''