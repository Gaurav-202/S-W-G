import random
print("This is a snake, water and gun game:\n")
l = ["snake", "water", "gun"]
n = 10
print("You have only 10 chances:\n")
c = 10
you = 0
comp = 0
while(n>0):
    a = random.choice(l)
    b = input("Enter your choice snake, water or gun?")
    if a == b:
        print("It is a draw")
    elif b == "snake" and a == "water":
        print("You are winner!")
        you = you +1
    elif b == "water" and a == "gun":
        print("You are winner!")
        you = you + 1
    elif b == "gun" and a == "snake":
        print("You won!")
        you = you + 1
    else:
        print("Oops, You lost")
        comp = comp +1
    n = n - 1
    c = c - 1
    print("Remaining chances: ", c)
    x = input("Do you want to quit? y/n: ")
    if x == "y":
        break
    else:
        continue
if you > comp:
    print("You defeated the computer!")
else:
    print("computer defeated you!")



