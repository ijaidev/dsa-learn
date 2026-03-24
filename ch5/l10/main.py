def exponential_growth(n, factor, days):
    seq = [n]
    for i in range(days):
        seq.append(n*(factor**(i+1)))
    return seq