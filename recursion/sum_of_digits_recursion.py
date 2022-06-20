def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n//10))

print(sum_of_digits(155))

#5 + sum_of_digits(15)
#5 + 5 + sum_of_digits(1)
##5 + 5 + 1 then returns 0


