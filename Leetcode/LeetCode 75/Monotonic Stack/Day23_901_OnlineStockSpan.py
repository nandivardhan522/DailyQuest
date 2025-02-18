class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.res=[]

    def next(self, price: int) -> int:
        i=0
        while i<len(self.stack):
            if(self.stack[-1-i]<=price):
                i+=self.res[-1-i]
            else:
                break
        self.stack.append(price)
        self.res.append(i+1)
        return i+1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''
Time Complexity:
Amortized O(1) per call to next() — Although the loop inside next() seems to have a complexity of 
O(n), each price is pushed and popped from the stack at most once. 
Hence, over multiple calls, the time complexity becomes amortized constant time.
Space Complexity:
O(n) — In the worst case, all prices are stored in the stack and res lists, where n is the number of next() calls.
'''