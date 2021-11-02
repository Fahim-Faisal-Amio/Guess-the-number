import random

Highest_range = input("Type a number: ")

if Highest_range.isdigit():
    Highest_range = int(Highest_range)

    if Highest_range <= 0:
        print('Please type a number larger than 0.')
        quit()
else:
    print('Please type a number.')
    quit()

random_number = random.randint(0, Highest_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("The guess is correct!")
        break
    elif user_guess > random_number:
        print("Guess is above the number!")
    else:
        print("Guess is below the number!")

print("You got it in", guesses, "guesses")
