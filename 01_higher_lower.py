# Lucky Unicorn Decompsition Step 1
# Get initial amount and check it's valid


#Integer checking function
def int_check(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! please enter an integer between {} and {}" .format(low, high)

        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# main routine gose here

how_mach = int_check("How much money do you want to play with ", 1, 10)
how_old = int_check("how old are you? ", 3, 120)