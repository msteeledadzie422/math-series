def fibonacci(n):
    return sum_series(n,0,1)


def lucas(n):
    return sum_series(n,2,1)


def sum_series(n, x=0, y=1):
    if n == 0:
        return x

    if n == 1:
        return y

    return sum_series(n-1,x,y) + sum_series(n-2,x,y)


print(fibonacci(5))
print(lucas(5))
print(sum_series(5,2,3))



