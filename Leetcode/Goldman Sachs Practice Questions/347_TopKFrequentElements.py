from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        countDict = Counter(nums)
        countList = []

        for i in countDict:
            countList.append([i, countDict[i]])

        countList.sort(key=lambda i: i[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(countList[i][0])

        return ans

Solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(Solution.topKFrequent(nums,k))


'''
Time Complexity:
    Counting elements (Counter(nums)) → O(n)
    Creating countList → O(n)
    Sorting countList → O(nlogn)
    Selecting top k elements → O(k)
    Total: O(nlogn) (due to sorting)

Space Complexity:
    countDict stores counts → O(n)
    countList stores frequency pairs → O(n)
    ans stores top k elements → O(k)
    Total: O(n)
'''