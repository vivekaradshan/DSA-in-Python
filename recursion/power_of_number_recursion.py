def power_of_number(x, n):
    assert (x >= 0 and int(x) == x) and (n >= 0 and int(n) == n), 'The number must be positive integer only!'
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * x**(n-1)

print(power_of_number(2, 1))