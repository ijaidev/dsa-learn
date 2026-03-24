def fib(n):
    if n <= 1:
        return n
    grandparent = 0
    parent = 1
    current = 0
    for _ in range(n-1):
        current = parent+grandparent
        parent, grandparent = current, parent
    return current

