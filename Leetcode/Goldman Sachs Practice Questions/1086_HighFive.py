from collections import defaultdict
class Solution:
    def highFive(self, items):
        d=defaultdict(list)
        l=set()
        for key,value in items:
            d[key].append(value)
            l.add(key)

        l=list(l)
        l.sort()
        res=[]
        print(d)
        for i in l:
            d[i].sort(reverse=True)
            val = sum(d[i][:5])//5
            res.append([i,val])
        return res

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

Solution = Solution()
print(Solution.highFive(items))

"""
Analysis:
Time Complexity:
    Building d and l (Set Insertion & List Append): O(n)
    Sorting Student IDs: O(klogk) where k is the number of unique students.
    Sorting Scores for Each Student: O(k⋅mlogm), where m is the max number of scores per student.
    Summing the Top 5 Scores: O(k).
    Total Complexity: O(n+klogk+kmlogm) → approximately O(nlogm) in worst case.
Space Complexity:
    d: Stores at most O(n) values.
    l: Stores at most O(k) values.
    res: Stores O(k) values.
    Total Complexity: O(n).
"""