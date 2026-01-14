#https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


#https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python

def sum_array(a):
    return sum(a)


#https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
    
#https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif b == "":
        return a
    elif a == "":
        return b
    else:
        return str(int(a) + int(b))

   
#https://www.codewars.com/kata/59342039eb450e39970000a6/train/python

def odd_count(n):
    return n // 2