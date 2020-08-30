# HL component 6 - statment Generator

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

    # Main routine

too_low = hl_statement("^^ Too low, try a higher number.    |   "
                       "Guesses Left: 3 ^^", "^")
print()
too_high = hl_statement("^^ Too low, try a lower number.    |   "
                       "Guesses Left: 2 vv", "v")
print()
duplicate = hl_statement("!! you already guessed that # pleacse try agian.    |   "
                         "Guesses Left: 2 !!", "!")
print()
well_done = hl_statement("*** Well done! you got it it in 3 guesses ***", "*")

print()
start_round = hl_statement("### round 1 of 3 ###", "3")