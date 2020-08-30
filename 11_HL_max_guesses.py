# HL component 11 - Manixmum Guseses Calculator

import math

for item in range(0, 4):    # loop component for easy tessting...

    low = int(input("low: "))  # use int check in due coure
    high = int(input("high ")) # use int check in due coure

    range = high - low + 1
    max_raw = math.log2(range)  # finds maximum # of guesses using brinary search
    max_upped = math.ceil(max_raw)  # round up (ceil --> ceiling)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()