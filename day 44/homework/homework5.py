def countBs(word):
    count = 0
    for char in word:
        if char == "B":
            count += 1
    return count

print(countBs("BEBBEB"))