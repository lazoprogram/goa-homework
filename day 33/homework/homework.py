def sum_numbers(x, y):
    return x + y

print(sum_numbers(10, 60))


def the_caller(n):
    return "Hello, World! " * n

print(the_caller(2))


def count_bs(text):
    return text.count("B")

print(count_bs("BarBeque"))


def sum_between_numbers(num1, num2):
    result = 0
    for i in range(num1, num2):
        result += i
    return result

print(sum_between_numbers(3, 10))


def letter_count():
    text = input("Enter Text: ")
    count = 0
    for i in text:
        if i != " ":
            count += 1
    return count

print(letter_count())


def returner(nums):
    return sum(nums) / len(nums)

print(returner([1, 3, 8, 5, 7]))


# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

def positive_sum(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i
    return result


# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python

def remove_char(s):
    if len(s) == 2:
        return ""
    return s[1:-1]


# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

def square_sum(numbers):
    result = 0
    for i in numbers:
        result += i ** 2
    return result


# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python

def find_smallest_int(arr):
    return min(arr)


# https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python

def string_to_number(s):
    return int(s)