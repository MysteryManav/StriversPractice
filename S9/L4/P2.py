# Stock Span Problem
class StockSpanner:
    def __init__(self):
        self.stock = []
    
    def next(self, price):
        span = 1
        while self.stock and self.stock[-1][0] <= price:
            span += self.stock.pop()[1]
        self.stock.append((price, span))
        return span

stockSpanner = StockSpanner()
print(stockSpanner.next(100))
print(stockSpanner.next(80))
print(stockSpanner.next(60))
print(stockSpanner.next(70))
