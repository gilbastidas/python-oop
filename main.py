import csv

from item import Item
from phone import Phone 
from keyboard import Keyboard

#item1 = Item("Phone", 100, 1)
#item2 = Item("Laptop", 1000, 3)
#item3 = Item("Cable", 10, 5)
#item4 = Item("Mouse", 50, 5)
#item5 = Item("Keyboard", 75, 5) 

# Get all attributes for Class level
#print(Item.__dict__)
#print("--------------------------")
# Get all attributes for Instance level
#print(item1.__dict__)
#print("--------------------------")

#item1.apply_discount()
#print(f"Price after discount: {item1.price}")
#print("--------------------------")

# Reasign pay rate to specific item
#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)
#print("--------------------------")

#print(Item.all)
#print("--------------------------")

#for instance in Item.all:
#    print(instance.name)
#print("--------------------------")

Item.instantiate_from_csv()
print("--------------------------")

#print(Item.all)
#print("--------------------------")

#print(Item.is_integer(7.0))
#print("--------------------------")

#phone1 = Phone("jscPhonev10", 500, 5, 1)
#phone2 = Phone("jscphonev20", 700, 5, 1)
#print("--------------------------")

#print(phone1.calculate_total_price())
#print("--------------------------")

#print(Item.all)
#print(Phone.all)

item1 = Item("MyItem", 750)
print(item1.name)
print("--------------------------")

item1.name = "OtherItem"
print(item1.name)
print("--------------------------")

item1.apply_discount()
print(item1.price)
print("--------------------------")

item1.send_email()
print("--------------------------")

item2 = Keyboard("Kboard", 100, 3)
item2.apply_discount()
print(item2.price)
print("--------------------------")

