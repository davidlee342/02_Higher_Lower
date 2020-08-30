# HL component 5 - no duplicates

# to do
# Set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL component 5 - prvents duplicates guesses

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess =""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace this with function call in due course

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("you already guesses that number! please try again. "
              "you still  have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

print(already_guessed)
