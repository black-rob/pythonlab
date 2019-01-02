#!/usr/bin/python
import calendar

month = int(raw_input("Gimme a month \n "))
year = int(raw_input("Gimme a year \n"))

cal = calendar.month(year, month)
print cal
