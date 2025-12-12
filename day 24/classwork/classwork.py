items = ["apple", "banana", "orange"]
print("საწყისი სია:", items)

items.append("grape")
print("append:", items)

items.insert(1, "kiwi")   
print("insert:", items)

items.remove("orange")
print("remove:", items)

items.pop(2)  
print("pop:", items)

print("სიის ზომა:", len(items))