def factorial(n):
    if n<2:               # hier is base case
        return 1
    return n*factorial(n-1) # hier is recursive case