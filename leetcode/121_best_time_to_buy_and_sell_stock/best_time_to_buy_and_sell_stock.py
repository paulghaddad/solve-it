# Time Complexity: O(n)
# Space Complexity: O(1)

def max_profit(prices):
    if len(prices) <= 1:
        return 0

    max_profit = 0
    lowest_price = prices[0]

    for _, current_price in enumerate(prices[1:]):
        if current_price < lowest_price:
            lowest_price = current_price

        if current_price - lowest_price > max_profit:
            max_profit = current_price - lowest_price

    return max_profit
