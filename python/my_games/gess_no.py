import random
import os
# from turtle import clear
print(" WELCOME TO MY FIRST GAME\n")
b=input("your choice E ,N ,H :-")
if (b=="E" or b=="e"):
    max=10
elif (b=="N" or b=="n"):
    max=100
elif (b=="H" or b=="h"):
    max=1000
a=random.randint(1,max)

print("Guess the Number from 1 to ",max)
# guess=10
for i in range(1,12):
    # os.system("clear")
    if i==11:
        print(f"Sorry..try again..\n Your Answer is: {a}\n Get Lost...........")
        break
    guess=int(input("Enter Your Number:-"))
    if guess >a:
        print("Your are higher")
    elif guess<a:
        print("Your are lesser")
    elif guess==a:
        print("Congratulations Your are Winner..")
        break   