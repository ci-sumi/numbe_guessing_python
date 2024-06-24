import random
guess=0
try:
    user_input = int(input("Enter a number:?"))
    while True:
        number_guess= random.randint(0,user_input)
        user_guess=int(input("Enter your guess:?"))
        guess+=1
        if(user_guess==number_guess):
            print("You are correct")
            break
        elif(user_guess<number_guess):
                print("The number you guessed is low")
        else:
                print("The numberyou guessed is too high")
                continue
    print(f" The number of guess {guess} ")
except ValueError:
    print("print a valid number")


