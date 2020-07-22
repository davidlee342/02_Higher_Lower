# HL component 3 - compares user guess with secret number

# to do
# Set up number of guesses
# Count # of gusses
# if user runs out of gusses, print  'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

SECRET = 7
GUESSES_ALLOWED = 4

# initialise variables
guesses_left = GUESSES_ALLOWED
num_won = 0
guess = ""

# Start game
while guess != SECRET and guesses_left >= 1:

    guess = int (input("Guess:  "))   # replace this with function call in dur cours
    guesses_left -= 1

    # If user has guesses left...
    if guesses_left >=
