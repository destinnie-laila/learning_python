teddy_bear_description = "Big cuddly teddy bear"
teddy_bear_price = 42.50

hard_toy_description = "Big rocket ship"
hard_toy_price = 50.0

soft_toy_description = "Rainbow soft ball"
soft_toy_price = 45.75

sales_tax = 0.050

#always define the total or descrition and set to null first
customer_one_total = 0

#to update the variables we just reuse them
customer_one_total += soft_toy_price

"""Remember that the += sign means also so variable 1 and also variable 2"""
customer_one_itemization = ""
customer_one_itemization += soft_toy_description

customer_one_total += hard_toy_price
customer_one_itemization +=hard_toy_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print('Customer Ones Items :')
print(customer_one_itemization)
print("customers total")
print(customer_one_total)