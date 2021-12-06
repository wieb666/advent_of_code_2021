import sys
import pandas as pd

class Board:
    """
    Create a bingo board
    """
    def __init__(self, rows) -> None:
        self.rows = rows
        self.board = pd.DataFrame(self.rows)

def create_boards(fname):
    bingo_numbers = False
    n = 0
    boards = []
    with open(fname) as f:
        rows = []
        for line in f:
            if not bingo_numbers:
                bingo_numbers = list(map(int, line.strip().split(",")))
                continue
            line = list(map(int, line.strip().split()))
            if n == 5:
                boards.append(Board(rows))
                n = 0
                rows = []
            else:
                if line == []:
                    continue
                rows.append(line)
                n += 1
        if n == 5:
            boards.append(Board(rows))
    return bingo_numbers, boards

def check_row_complete(board):
    return board.board.loc[(board.board.sum(axis=1) == 0)].empty

def check_col_complete(board):
    return board.board.loc[(board.board.sum(axis=0) == 0)].empty


def main(fname):
    bingo_numbers, boards = create_boards(fname)
    won = False
    last_num = None
    winning_board = None
    for n in range(len(bingo_numbers)):
        if won == True:
            break
        for i in range(len(boards)):
            board = boards[i]
            if not check_row_complete(board=board) or not check_col_complete(board=board):
                last_num = bingo_numbers[n-1]
                winning_board = i
                won = True
                break
            board.board.replace(bingo_numbers[n], 0, inplace=True)

    print(last_num)
    print(boards[winning_board].board.values.sum())
    
    print(last_num * boards[winning_board].board.values.sum())

if __name__ == "__main__":
    main(sys.argv[1])
