
# Programming to calculate total stock in a company

# Product list
prods = [['wax', '3000kshs', '30000'], 
         ['spatula', '500kshs', '2000'], 
         ['strips', '4500kshs', '3590'], 
         ['gloves', '500kshs', '7500']]


total_stock = 0

for item in prods:

    stock = int(item[-1])
    total_stock += stock


print("Total stock in company:", total_stock)
