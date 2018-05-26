def checkio(game_result):

    # create entries for columns (down results)
    columns = ["".join(col) for col in list(zip(*game_result))]
    
    # create angle entries from top left to bot right
    # and bot left to top right
    top_left = ""
    bot_left = ""
    for n in range(0, 3):
        top_left += game_result[n][n]
        bot_left += game_result[2-n][n]

    # add all entries to original results
    game_result += columns
    game_result += [top_left, bot_left]

    # test results
    if "XXX" in game_result:
        return "X"
    if "OOO" in game_result:
        return "O"
    return "D"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
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

