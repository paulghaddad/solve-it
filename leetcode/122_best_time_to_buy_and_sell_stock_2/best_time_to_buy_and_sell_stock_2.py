# Time Complexity: O(n)
# Space Complexity: O(1)

def max_profit(prices):
    profits = 0

    for i in range(len(prices)-1):
        change_in_price = prices[i+1] - prices[i]
        if change_in_price > 0:
            profits += change_in_price

    return profits
