def decimal_to_binary(num: int ):
    assert (int(num) == num), 'The number must be integer only!'
    if num == 0:
        return 0
    else:
        return num%2 + 10 * decimal_to_binary(int(num/2))
        #1+10*(0) + 10*1 + 10*1 = 1+0+10+10

print(decimal_to_binary(13))

#13%2 -> 1
#6%2 -> 0
#3%2 -> 1
#1