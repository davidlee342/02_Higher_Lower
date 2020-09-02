# HL component 10 - loop Game

# To Do
# Loop entire game...

keep_going = ""
if __name__ == '__main__':
    while keep_going == "":

        SECRET = 7
        GUESSES_ALLOWED = 4

        rounds = int(input("How many rounds? "))   # replace with int check
        game_stats = []

        num_won = 0
        rounds_played = 0

        while rounds_played < rounds:
            print()
            print("**** Round {} *****".format(rounds_played + 1))
            guess = ""
            gueeses_left = GUESSES_ALLOWED
            rounds_played += 1

            while guess != SECRET and gueeses_left >= 1:

                guess = int(input("Guess: "))  # replace this with function call in due course
                gueeses_left -= 1

                if gueeses_left >= 1:

                    if guess < SECRET:
                        print("Too low, try a lower number.  Guesses left {}".format(gueeses_left))

                    elif guess > SECRET:
                        print("Too high, try a higher number.  Guesses left {}".format(gueeses_left))
                else:
                    if guess < SECRET:
                        print("Too low")
                    elif guess > SECRET:
                        print("Too high")

            if guess == SECRET:
                if gueeses_left == GUESSES_ALLOWED - 1:
                    print("Amazing!  You  got it in one guess")
                else:
                    print("Well done, you got it in {} guesses".format(GUESSES_ALLOWED))
                    num_won += 1
            else:
                print("Sorry - you lose this round as you have run out of guesses ")
                gueeses_left -= 1  # penalty point for losing

                game_stats.append(GUESSES_ALLOWED - gueeses_left)
                print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1 ))
                rounds_played += 1

        print()
        keep_going = input("Press <enter to play again or any key to quit")

#print each  round's outcome..
    print()
    print("*** Game scores ***")
    list_count = 1
    for item in game_stats:

        # indicastes if game has been won or lost
        if item > GUESSES_ALLOWED:
            status = "lost, ran out of guesses"
        else:
            status = "won"

        print("Rounds {}: {} ({})".format(list_count, item, status))
        list_count += 1

        # Calculate (and then print) game statistics
        game_stats.sort()
        best = game_stats[0]   # frist item in sorted list
        worst = game_stats[-1] # last item in sorted list
        average = sum(game_stats)/len(game_stats )

        print()
        print("*** Summary Statistics ***")
        print("Best: {}".format(best))
        print("Average: {:.2f}".format(average))

        print()
        keep_going = input("press <enter> to play again or any to quit: ")

        print("Thank you for playing. Good bye")
