
my_list = [5, 12, 7, 9, 20, 33, 42, 18, 27, 14, 8, 6, 3, 11, 30]


two = my_list[:len(my_list)//2], my_list[len(my_list)//2:]
three = my_list[:len(my_list)//3], my_list[len(my_list)//3:2*len(my_list)//3], my_list[2*len(my_list)//3:]
four = my_list[:len(my_list)//4], my_list[len(my_list)//4:len(my_list)//2], my_list[len(my_list)//2:3*len(my_list)//4], my_list[3*len(my_list)//4:]
five = my_list[:len(my_list)//5], my_list[len(my_list)//5:2*len(my_list)//5], my_list[2*len(my_list)//5:3*len(my_list)//5], my_list[3*len(my_list)//5:4*len(my_list)//5], my_list[4*len(my_list)//5:]


without_first5 = my_list[5:]
without_last7 = my_list[:-7]


neg1 = my_list[-5]
neg2 = my_list[-10:-5]
neg3 = my_list[:-10]


print("Two parts:", two)
print("Three parts:", three)
print("Four parts:", four)
print("Five parts:", five)
print("Without first 5:", without_first5)
print("Without last 7:", without_last7)
print("Negative slices:", neg1, neg2, neg3)
