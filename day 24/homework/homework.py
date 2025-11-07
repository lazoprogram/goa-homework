nums = [3, 8, 11, 14, 17, 22, 25, 30, 33, 40]
for n in nums:
    if n % 2 != 0:
        print(n)






nums = [2, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
for n in nums:
    if n % 2 == 0:
        print(n)







guests = ["ანა", "ნიკა", "გიორგი", "მარი", "სოფო"]
print("საწყისი სია:", guests)

removed = guests.pop(1)  # ამოშალე ნიკა
guests.append("ლუკა")    # დაამატე ლუკა
guests.insert(0, "ლაზარე") # დაამატე თაკო დასაწყისში

print("ამოშლილი:", removed)
print("დამატებულები: ლაზარე, ლუკა")
print("სულ დარჩა:", len(guests))
print("საბოლოო სია:", guests)



nums = [2, 3, 4, 5, 6, 7, 8]
s = 0
for n in nums:
    if n % 2 == 0:
        s += n
print("ჯამი", s)



names = ["ნიკა", "ანა", "გიორგი", "სოფო", "ლუკა"]
mine = "ლაზარე"

found = False
for n in names:
    if n == mine:
        print("ნაპოვნია", n)
        found = True

if not found:
    print("Not Found")






fruits = ["ვაშლი", "ბანანი", "მანგო", "ატამი", "ყურძენი", "მსხალი", "კივი", "ფორთოხალი", "საზამთრო", "მარწყვი"]


fruits.pop(9)
fruits.pop(7)
fruits.pop(5)


fruits.append("ანანასი")

top5 = fruits[:5]
print("ჩემი TOP 5:", top5)



#ბონუს

subjects = ["მათემატიკა", "ინგლისური", "ფიზიკა", "ბიოლოგია", "გეოგრაფია"]
total = 0

for subject in subjects:
    grade = int(input(subject + "-ის ქულა: "))
    total += grade

avg = total / len(subjects)
print("საშუალო ქულა", avg)



