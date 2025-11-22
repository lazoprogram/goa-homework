# print() - ჩვენ შეგვიძლია პირდაპირ გამოვიძახოთ ფუნქცია და არ ჩავსვათ print()-ში
# return - ჩვენ შეგვიძლია ფუნქციაში დავაბრუნოთ მონაცემი და შემდეგ ან ცვლადში შევინახოთ ან სხვა ფუნქციას გადავცეთ არგუმენტად

def check_age(num1):
   if num1 >= 18:
        return "Access Granted"
   else:
        return "Access Denied"
    
print(check_age(15))



def user_info(name, surname, address):
    return f"ჩემი სახელი არის {name}", f"ჩემი გვარი არის {surname}", f"ჩემი მისამართი არის {address}"

print(user_info("ლაზარე", "მამუჩაშვილი", "საქართველო"))


def argument(num1, num2):
    return num1 ** num2

print(argument(2, 3))



def arithmetic_average(arr):
    return sum(arr) / len(arr)

print(arithmetic_average([12, 15, 18, 20 ,5]))