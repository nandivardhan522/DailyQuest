import heapq
from collections import defaultdict
class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.addedIntegers = []
        self.is_present = set()

    def popSmallest(self) -> int:
        if (len(self.addedIntegers)):
            answer = heapq.heappop(self.addedIntegers)
            self.is_present.remove(answer)
        else:
            answer = self.smallest
            self.smallest += 1
        return answer

    def addBack(self, num: int) -> None:
        if (self.smallest <= num or num in self.is_present):
            return

        heapq.heappush(self.addedIntegers, num)
        self.is_present.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

'''
Time Complexity:
    popSmallest():If addedIntegers (min-heap) is not empty, heapq.heappop() takes O(logN).
    If addedIntegers is empty, we just increment smallest, which takes O(1).
    Worst-case complexity: O(logN).
    addBack(num): Checking conditions (num >= self.smallest or num in self.is_present): O(1).
    Inserting into heap (heapq.heappush()): O(logN).
    Inserting into set (is_present.add(num)): O(1).
    Overall worst-case complexity: O(logN).
    Thus, for Q total operations, the worst-case complexity is O(QlogN).
    
Space Complexity:
    self.smallest: O(1) (single integer).
    addedIntegers (min-heap): O(N) (stores at most N elements).
    is_present (set): O(N) (tracks numbers in the heap).
    Total space complexity: O(N).
'''