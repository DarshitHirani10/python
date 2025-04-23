import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q): ")
    if(userChoice == "Q", "q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success: Correct Guess!!")
        break
    elif(userChoice < target):
        print("ypur number was to small. Take a bigger guess..")
    else:
        print("ypur number was to big. Take a smaller guess..")


print("--------Game Over--------")