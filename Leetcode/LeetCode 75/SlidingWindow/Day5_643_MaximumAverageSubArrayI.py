class Solution:
    def findMaxAverage(self, nums,k):
        max_avg=float('-inf')
        if(len(nums)<k):
            return 0
        if(len(nums)==k):
            return sum(nums)/k
        i=0
        j=k-1
        temp=sum(nums[i:j])
        while(j<len(nums)):
            temp+=nums[j]
            avg=temp/k
            max_avg=max(avg,max_avg)
            temp=temp-nums[i]
            i+=1
            j+=1
        return max_avg
nums = [1,12,-5,-6,50,3]
k = 4
sol=Solution()
print(sol.findMaxAverage(nums,k))
'''
Complexity Analysis:
    Time Complexity:
        Calculating the initial sum for the first k elements takes O(k).
        The sliding window involves n−k iterations, each of which involves a constant amount of work. 
        Total complexity: O(n)
    Space Complexity:
        Only a constant amount of extra space is used for variables (temp, max_avg, i, j). 
        Space complexity: O(1)
'''