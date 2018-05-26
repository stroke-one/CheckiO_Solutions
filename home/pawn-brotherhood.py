def safe_pawns(pawns: set) -> int:
    board = {x: [] for x in range(1, 9)}
    safes = 0

    for pos in pawns:
        pos_int = split_position(pos)
        board[pos_int[1]].append(pos_int[0])

    for row in range(2, 9):
        for col in range(1, 9):
            if col in board[row]:
                if (col - 1 in board[row - 1]) or (col + 1 in board[row - 1]):
                    safes += 1
    return safes

def split_position(pos: str):
    return (ord(pos[0])-96, int(pos[1]))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
