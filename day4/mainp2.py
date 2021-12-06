import sys
import pandas as pd

class Board:
    """
    Create a bingo board
    """
    def __init__(self, rows) -> None:
        self.rows = rows
        self.board = pd.DataFrame(self.rows)
        self.won = False
        self.number = None

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
    winning_order = dict()
    won_last = None
    for n in range(len(bingo_numbers)):
        for i in range(len(boards)):
            try:
                board = boards[i]
                if not check_row_complete(board=board) or not check_col_complete(board=board):
                    if board not in winning_order.keys():
                        winning_order[board] = [board.board, bingo_numbers[n - 1]]
                else:
                    board.board.replace(bingo_numbers[n], 0, inplace=True)
            except IndexError:
                break

    won_board = winning_order[list(winning_order.keys())[-1]][0]
    won_last = winning_order[list(winning_order.keys())[-1]][1]
    
    print(won_last * won_board.values.sum())

if __name__ == "__main__":
    main(sys.argv[1])
