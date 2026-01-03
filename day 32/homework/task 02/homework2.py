def count_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    text = text.lower()
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1
    return count

print(count_vowels("lazare"))


def find_max(nums):
    nums.sort()
    return nums[-1]

print(find_max([2,1,7,3,19,4,20,7]))


def reverse_string(string):
    result = ""
    for i in range(len(string)-1, -1, -1):
        result += string[i]
    return result

print(reverse_string("python"))


def count_pos_neg(nums):
    count_pos = 0
    count_neg = 0
    for i in nums:
        if i > 0:
            count_pos += 1
        elif i < 0:
            count_neg += 1
    return [count_pos, count_neg]
           
print(count_pos_neg([1,-2,3,-4,0,5]))


def is_palindrome(string):
    return string == reverse_string(string)

print(is_palindrome("level"))
print(is_palindrome("python"))