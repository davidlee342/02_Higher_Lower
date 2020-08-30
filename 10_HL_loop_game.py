# HL component 10 - loop Game

# To Do
# Loop entire game...

keep_going = ""
while keep_going == "":

    SECRET = 7
    GUESSES_ALLOWED = 4

    rounds = int(input("How many rounds? "))   # replace with int check
    game_stats = []

    num_won = 0
    round_played = 0

    while round_played < rounds:
        guess = ""
        gueeses_left = GUESSES_ALLOWED

        while guess != SECRET and gueeses_left >= 1:

            guess = int(input("Guess: "))  # replace this with function call in due course
            gueeses_left -= 1

            if gueeses_left >= 1:

                if guess < SECRET:
                    print("Too high, try a lower number.  Guesses left {}".format(gueeses_left))

                elif guess > SECRET:
                    print("Too low, try a higher number.  Guesses left {}".format(gueeses_left))
            else:
                if guess < SECRET:
                    print("Too high")
                elif guess > SECRET:
                    print("Too low")

        if guess == SECRET:
            if gueeses_left == GUESSES_ALLOWED - 1:
                print("Amazing!  You  got it in one guess")

