#!/usr/bin/python3

import random
print("Welcome, Who's paying the bill today")
names_strings = input("give me everybody's name, seperated by a comma.")
names = names_strings.split(", ")
num_items = len(names)
the_choice = random.randint(0, (num_items - 1))
payment = names[the_choice]
print(f"{payment} is going to pay for the food")

