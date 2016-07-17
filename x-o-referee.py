def checkio(game_result):

    # intialize 'Draw' by default
    decision = "D"

    # check the easy case first - matching by row
    for row in game_result:
        if row == 'XXX':
            decision = 'X'
        elif row == 'OOO':
            decision = 'O'

    # now check the diagonals
    diag1 = game_result[0][0] + game_result[1][1] + game_result[2][2]
    diag2 = game_result[0][2] + game_result[1][1] + game_result[2][0]

    if diag1 == 'XXX' or diag1 == 'OOO' or diag2 == 'XXX' or diag2 == 'OOO':
        decision = game_result[1][1]

    # finally, check the columns
    col1 = game_result[0][0] + game_result[1][0] + game_result[2][0]
    col2 = game_result[0][1] + game_result[1][1] + game_result[2][1]
    col3 = game_result[0][2] + game_result[1][2] + game_result[2][2]

    if col1 == 'XXX' or col2 == 'XXX' or col3 == 'XXX':
        decision = 'X'
    elif col1 == 'OOO' or col2 == 'OOO' or col3 == 'OOO':
        decision = 'O'

    return decision

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

