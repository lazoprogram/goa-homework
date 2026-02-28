# https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/python


def get_age(age):
    return int(age[0])

#https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python

def remove_char(s):
    if len(s) == 2:
        return ""
    return s[1:-1]


#https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python


def is_palindrome(s):
        return s.lower() == s[::-1].lower()


#https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python


def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"