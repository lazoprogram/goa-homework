#https://www.codewars.com/kata/55f1b763dd670651620000ce/train/python

def count_char_occurrences(strng, char):
    return strng.count(char)


#https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python

def paperwork(n, m):
    if n < 0:
        return 0
    elif m < 0:
        return 0
    return n * m


#https://www.codewars.com/kata/5a360620f28b82a711000047/train/python

def define_suit(card):
    for i in card.lower():
        if i == "c":
            return "clubs"
        elif i == "d":
            return "diamonds"
        elif i == "h":
            return "hearts"
        elif i == "s":
            return "spades"
        
        
#https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python

def distinct(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)
    return result