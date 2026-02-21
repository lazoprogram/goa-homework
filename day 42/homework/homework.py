#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

def sum_array(arr):
    if arr == None or  len(arr) <= 1:
        return 0
    arr.remove(min(arr))
    arr.remove(max(arr))
    return sum(arr)


#https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python

def find_smallest_int(arr):
    return min(arr)