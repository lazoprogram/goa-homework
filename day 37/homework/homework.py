#https://www.codewars.com/kata/55f1b763dd670651620000ce/train/python

def count_char_occurrences(strng, char):
    return strng.count(char)


#https://www.codewars.com/kata/56efc695740d30f963000557/train/python

def to_alternating_case(string):
    return string.swapcase()


#https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/python

def get_volume_of_cuboid(length, width, height):
    return length * width * height


#https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"