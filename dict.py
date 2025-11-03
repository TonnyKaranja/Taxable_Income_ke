person = [
    "name","joy",
    "age",26,
    "married",False,
    "address","123 view parks utalii st",
    "friends",{"mark","lorri"}
]
print(person)
                                                                

my_ds = [23, "jane"], (560), {"lesson", "maths", "currency", "kes"}, 987, 76, "john"
# checks if "kes" is in the set
print("kes" in my_ds[2])
print(my_ds)
print(560)

(
  [23, "jane"],           # a list
  560,                    # an integer
  {"lesson", "maths", "currency", "kes"},  # a set
  987,                    # integer
  76,                     # integer
  "john"                  # string
)
my_ds = [23, "jane"], (560), {"lesson", "maths", "currency", "kes"}, 987, 76, "john"

# Convert to a list so we can modify
x= list(my_ds)
 # last element ("john") becomes "jane"
x[-1] = "jane"  
my_ds = tuple(x)

print(my_ds)
print(len(my_ds))

                                                                  
                                                                    