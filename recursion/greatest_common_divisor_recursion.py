def gcd(num1: int, num2: int):
    assert (int(num1) == num1 and int(num2) == num2), 'The number must be integer only!'
    if num1 < 0:
        num1 *= -1
    if num2 < 0:
        num2 *= -1
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)

print(gcd(-1.8,-48))

# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a%b)
