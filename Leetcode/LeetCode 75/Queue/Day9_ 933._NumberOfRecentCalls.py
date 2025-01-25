class RecentCounter:

    def __init__(self):
        self.counter=[]

    def ping(self, t: int) -> int:
        self.counter.append(t)
        while((self.counter[-1] - self.counter[0])>3000):
            self.counter.pop(0)
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:

'''
Complexity Analysis
    Time Complexity:
        The ping method:Appends a timestamp (O(1)).
        Uses a while loop to remove outdated timestamps from the front of self.counter.
        In the worst case, all timestamps in self.counter might need to be removed. 
        Thus, the complexity of the while loop is amortized O(1) across multiple calls since each timestamp is added and removed at most once.
        Overall, the time complexity per ping call is O(1) (amortized).
    Space Complexity:
        The self.counter list stores at most n timestamps, where n is the number of pings in the last 3000 ms.
        The space complexity is O(n).
'''