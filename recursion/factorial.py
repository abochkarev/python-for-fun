# calculate factorial
def fact(n):
    return n if n == 1 else fact(n - 1) * n


print
fact(5)
