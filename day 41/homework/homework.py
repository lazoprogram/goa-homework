#https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python

def array_plus_array(arr1,arr2):
    return (sum(arr1) + sum(arr2))


#https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump


#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python


def sum_array(arr):
    if arr == None or  len(arr) <= 1:
        return 0
    arr.remove(min(arr))
    arr.remove(max(arr))
    return sum(arr)


#https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python


def double_char(s):
    result = ""
    for i in s:
        result += i * 2
    return result


#https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/python


def is_even(n): 
    return n % 2 == 0