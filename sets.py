number = {1,1,2,3,4,5}
print(number)
print(type(number))

#acessing set items
numbers = {110,73,709,53}
print(numbers)
print(709 in numbers)

#adding a single item
numbers.add("mexico")
print(numbers)

#adding multiple items
numbers.update({505,808,909,})
print(numbers)

#removing set items
numbers.remove(505)
print(numbers)

#discarding sets in an item
number.discard(808)
print(number)

#clear
numbers.clear()
print(numbers)