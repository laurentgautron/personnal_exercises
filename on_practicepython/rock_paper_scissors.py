""" Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner, and ask if the players want to start a new game)
"""

to_continue = ""
list_item = {1:"rock", 2:"paper", 3:"scissors"}
while True:
    if to_continue == "n":
        print("Ok bye")
        break
    gamer1 = int(input("First gamer must choose :\n- 1 = rock\n- 2 = paper\n- 3 = scissors\nYour choice: "))
    gamer2 = int(input("second gamer must choose :\n- 1 = rock\n- 2 = paper\n- 3 = scissors\nYour choice: "))
    if gamer1 == gamer2:
        print("nobody win !!!")
    elif (gamer1 == 1) and (gamer2 == 3):
        print("The {} wins !!!".format(list_item[gamer1]))
    elif (gamer1 == 2) and (gamer2 == 1):
        print("The {} wins !!!".format(list_item[gamer1]))
    elif (gamer1 == 3) and (gamer2 == 2):
        print("The {} wins !!!".format(list_item[gamer1]))
    else:
        print("The {} wins !!!".format(list_item[gamer2]))
    to_continue = input(" an other game ? (y/n): ")
    while to_continue not in ("n", "y"):
        print("you tap: ", to_continue)
        to_continue = input(" an other game ? (y/n): ")
