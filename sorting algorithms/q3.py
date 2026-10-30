def selection_sort(prices):
    n = len(prices)

    for i in range(n - 1):
        minimum_index = i

        for j in range(i + 1, n):
            if prices[j] < prices[minimum_index]:
                minimum_index = j

        prices[i], prices[minimum_index] = prices[minimum_index], prices[i]
        print(
            f"Pass {i + 1}: minimum = {prices[i]}, array = {prices}"
        )


prices = [499, 150, 799, 250, 100]
selection_sort(prices)