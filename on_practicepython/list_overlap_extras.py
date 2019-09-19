""" Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
 (without duplicates). Make sure your program works on two lists of different sizes. Randomly generate two lists to
 test this. Write this in one line of Python"""

from random import randint

a = []
b = []
for x in range(1, 12):
    a.append(randint(1, 101))
for x in range(1, 25):
    b.append(randint(1, 101))
a = list(set(a))
b = list(set(b))
list_overlap = [elements for elements in a if elements in b]
print("the a list is:", a)
print("the b list is: ", b)
print(list_overlap)
