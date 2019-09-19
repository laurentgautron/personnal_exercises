""" Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of
Python that takes this list a and makes a new list that has only the even elements of this list in it."""

import random

list_c = []
size_list = random.randint(5, 25)
while len(list_c) < size_list:
    list_c.append(random.randint(1, 100))
even_list = [elements for elements in list_c if elements % 2 == 0]
print("the list to sort: ", list_c)
print("the list sorted: ", even_list)
