result = 0
for i in range(1, 100):
    if i % 2 != 0:
        result += i
print(result)


result_2 = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        result_2 += i
    i += 1
print(result_2)


number = int(input("Enter Number: "))
while number % 2 != 0:
    number = int(input("Enter Number: "))
print("You enter an even number and the loop is over")


number2 = int(input("Enter Number: "))
if number2 > 0:
    print("დადებითია")
elif number2 < 0:
    print("უარყოფითი")
else:
    print("რიცხვი არის 0")


num3 = int(input("enter Number: "))
if num3 % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")


score = int(input("text score: "))
if score >= 90 and score <= 100:
    print("A-ფრიადი")
elif score >= 70 and score <= 89:
    print("B-კარგი")
elif score >= 50 and score <= 69:
    print("C-დამაკმაყოფილებელი")
elif score >= 0 and score <= 49:
    print("ჩაიჭრა")
else:
    print("შემოიყვანეთ სწორი ქულა")