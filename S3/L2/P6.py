# Stock Buy and Sell: Return the maximum profit that can be made by buying a stock in single day and selling it in future
def stock_buy_sell(array):
    max_profit = 0
    min_buy_price = array[0]
    buy_val = 0
    sell_val = 0
    for i in range(1, len(array)):
        min_buy_price = min(min_buy_price, array[i])
        max_profit = max(max_profit, array[i] - min_buy_price)
    return max_profit

array = [7, 1, 5, 3, 6, 4]
print(stock_buy_sell(array))
