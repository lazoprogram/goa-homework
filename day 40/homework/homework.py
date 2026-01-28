#https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

def summation(num):
    result = 0
    for i in range(0, num+1):
        result = result + i
    return result



#https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2



#https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python

def invert(l):
    list = []
    for i in l:
        if i:
            list.append(-i)
    return list



#https://www.codewars.com/kata/54edbc7200b811e956000556/train/python

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count



#https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2