import random
print("Welcome to the game: )")
num_range=input("Enter a number ")

if num_range.isdigit():
    num_range=int(num_range)
else:
    print("Please enter a number next time ")
    quit()
number=random.randint(0,num_range)
guesses=0
while True:
    guesses+=1
    user_guess=input("Enter the guess number ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter a number next time ")
        continue

    if(number==user_guess):
        print(f"You got it!\nYour guess is {user_guess} and Computer guess is also {number}")
        break

    else:
        if(user_guess>number):
            print("Enter a lower number")
        else:
            print("Enter a Greater number")

#shehroz
print(f"You got right guess in {guesses} times")
