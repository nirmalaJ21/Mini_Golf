import math

my_Name = input(f"Welcome to GC mini golf! What is your name?")
hole_type = input(f"Hi {my_Name}, Would you like to play 3 or 6 holes?")

total = 0
putts = []

if hole_type == "3":
    for i in range(3):
        putts_count = input(f"How many putts for hole {i + 1}? (par: 3) ")
        putts.append(int(putts_count))
        total = sum(putts)

        if (i >= 2):
            if (total == 9):
                print(f"Good game, {my_Name}. Your total score was: 0.")

            elif total < 9:
                total = 9 - total
                print(f"Great job, {my_Name},! Your total score was: -{total}")
            else:
                print(f"Nice try, {my_Name}... Your total score was:  +{total}.")
else:
    for i in range(6):

        putts_count = input(f"How many putts for hole {i + 1}? (par: 3) ")
        putts.append(int(putts_count))
        total = sum(putts)

        if (i >= 5):
            if (total == 18):
                print(f"Good game, {my_Name}. Your total score was: 0.")

            elif total < 18:
                total = 18 - total
                print(f"Great job, {my_Name},! Your total score was: -{total}")
            else:
                print(f"Nice try, {my_Name}... Your total score was:  +{total}.")
