from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)
        occurrences = set(freq.values())
        print(freq)
        return len(occurrences) == len(freq)

sol=Solution()
arr = [1,2,2,1,1,3]
print(sol.uniqueOccurrences(arr))
'''
Time Complexity:
    Counting elements: O(n).
    Creating a set of frequencies: O(m), where m=len(freq).
    Overall Time Complexity: O(n).

Space Complexity:
    The Counter object and set of frequencies each require O(m) space.
    Overall Space Complexity: O(n).
'''
