def is_adult(age):
    if age >= 18:
        return "adult"
    else:
        return "Minor"
    



def max_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    



def calculate_age(birth):
    current_year = 2026
    age = current_year - birth
    return age


print(calculate_age(1994))