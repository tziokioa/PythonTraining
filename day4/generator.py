def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn(7)))