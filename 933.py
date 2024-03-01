class RecentCounter:
    stocks=[]
    def __init__(self):
        self.stocks=[]
    def ping(self, t: int) -> int:
        self.stocks.append(t)
        while self.stocks[0]<t-3000:
            self.stocks.pop(0)
        return len(self.stocks)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)