items = ["mary", 12.856, True, 108, "this is the last items"]
print(items)
print(type(items))
print(items[0])
print(items[0][0])
print(items[-1])
values = [1,2,3,[4,5,6],[7,8,9],["x","y"],10]
print(len(values))
values.append(105)
print(values)
values.extend(["mango","apple","yogurt"])
print(values)
values.insert(5,"icecream")
print(values)
values.remove([4,5,6])
print(values)
values.pop()
print(values)
values.pop(5)
print(values)
values.clear()
print(values)
#count()
cars = ["toyota","bmw","lexus"]
print(cars)
x = cars.count("lexus")
print(x)
#sort()
cars = ["toyota","bmw","lexus"]
cars.sort()
print(cars)
#reverse())
cars = ["toyota","bmw","lexus"]
cars.reverse()
print(cars)
#copy()
cars = ["toyota","bmw","lexus"]
thislist = ["toyota","bmw","lexus"]
mylist = thislist.copy()
print(mylist)
mylist = ("toyota","bmw","lexus")
print(mylist)
#joining list, method one is concatenation +
list1 = ["toyota","bmw","lexus"]
list2 = ["nissan","mazda","ford"]
list3 = list1 + list2
print(list3)
#joining list, method 2 is append
list1.append(list2)
print(list1)
#joining list, method 3 is extend
list1.extend(list2)
print(list1)
#index()
values = ["a","a","b","c"]
i = values.index("a")
print(i)