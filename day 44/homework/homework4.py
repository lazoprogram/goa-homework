def sumDigits(number):
    total = 0
    for i in str(number):
        total += int(i)
    return total

print(sumDigits(12))