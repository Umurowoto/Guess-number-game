secret_number = 5
i = 0

# give the user 3 chances to guess the number
while i <=3:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("congratulations! You guessed the number.")
        break
    else:
        print("Sorry, that's not correct. Try again.")




