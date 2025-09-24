#Natasha Foreman
#9/20/25
#Assignment 1_3
#To create a code for "Bottles of beer"

def countdown(n):
    while n > 0:
        print(f"{n} bottle(s) of beer on the wall, {n} bottle(s) of beer.")
        n -= 1
        print(f"Take one down and pass it around, {n} bottle(s) of beer on the wall.\n")
    print("Time to buy more bottles of beer.")

n = int(input("Enter number of bottles:"))
countdown(n)
