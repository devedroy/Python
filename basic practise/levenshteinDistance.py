
def seq_sum(start, stop):
    return(start + stop - 1) * (stop - start) // 2
    
def highestProfit(numSuppliers, inventory, order):
    # WRITE YOUR CODE HERE
    count = sorted(Counter(inventory).items(), reverse=True)
    suppliers = 0
    profit = 0
    left = order
    
    for i, (stock, extra) in enumerate(count):
        # TODO: write code...
        next_stock = count[i + 1][0] if i < len(count) - 1 else 0
        suppliers += extra
        supply = suppliers * (stock - next_stock)
        full, part = divmod(min(left, supply), suppliers)
        profit += suppliers * seq_sum(stock - full + 1, stock + 1)  \
        + part * (stock - full)
        left -= supply
        if left <= 0:
            break
    return profit