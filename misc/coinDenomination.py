coin_denominations = [25, 10, 5, 1]

def make_change(change_needed): 
    change = []
    sum = 0 
    for coin in coin_denominations: 
        while sum + coin <= change_needed: 
            sum += coin 
            change.append(coin) 
    return change 



