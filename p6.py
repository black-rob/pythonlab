#!/usr/bin/python
# only works in ptyhon 
values = input("Input some comma seprated numbers : ")
# values get placed into value variable
list = values.split(",")
# tuple = tuple(list)
# this line converts the list into a tuple, looks like how int does input
print('List : ', list)
# print('Tuple : ', tuple)

# For Python 2.7, given solution does not work.
# It gives error as: AttributeError: 'tuple' object has no attribute 'split'
#
# You can solve this exercise as follows:
#
# values = input("Enter comma separated numbers :")
#
## When you assign single variable to multiple inputs then it becomes tuple.
#
# print 'tuple',values #This will print tuple
#
## To print list convert tuple into list
#
# print 'List=', list(values)
