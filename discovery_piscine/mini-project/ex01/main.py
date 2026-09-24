import sys
from checkmate import check_board, explain

USAGE = "usage: python3 main.py [--explain] board.chess [board2.chess ...]"


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None


def main():
    args = sys.argv[1:]
    show = "--explain" in args
    files = [a for a in args if a != "--explain"]
    if not files:
        print(USAGE, file=sys.stderr)
        return

    for path in files:
        board = read_file(path)
        result = check_board(board)
        if result is None:
            print("Error")
            continue
        print("Success" if result else "Fail")
        if show:
            print(explain(board))
            print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
