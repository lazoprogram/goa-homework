# > - გამოიტანს True-ს თუ ერთი რიცხვი მეორეზე მეტია 
# < - გამოიტანს True-ს თუ ერთი რიცხვი მეორეზე ნაკლებია
# >= - გამოიტანს True-ს თუ ერთი რიცხვი მეორეზე მეტია ან ტოლია
# <= - გამოიტანს True-ს თუ ერთი რიცხვი მეორეზე ნაკლებია ან ტოლია
# == - გამოიტანს True-ს თუ ერთი რიცხვი მეორეს ტოლია
# != - გამოიტანს True-ს თუ ერთი რიცხვი მეორეს ტოლი არ არის
# and - გამოიტანს True-ს თუ ორი პირობა სწორია
# or - გამოიტანს True-ს თუ ერთ-ერთი პირობა მაინც არის სწორი


num = int(input('Enter random number: '))
print(num % 2 == 0)


login = 'luka123'
password = '12345678luka'
user_login = input('Enter login: ')
user_password = input('Enter password: ')
print('Access:', user_login == login and user_password == password)


age = int(input("enter your age: "))
height = int(input("enter your height: "))
weight = int(input("enter your weight: "))
print("can go to millitary:", age >= 18 and height >= 170.5 and weight >= 55.5)