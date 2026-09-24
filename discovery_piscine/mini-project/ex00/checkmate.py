PIECES = "KQBRP"


def _parse(board):
    if not isinstance(board, str):
        return None
    lines = board.splitlines()
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    size = len(lines)
    if size == 0:
        return None
    for line in lines:
        if len(line) != size:
            return None
    return lines


def _find_king(grid):
    king = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "K":
                if king is not None:
                    return None
                king = (r, c)
    return king


def _is_in_check(grid, kr, kc):
    size = len(grid)

    # Pawn: captures diagonally upward, so it attacks the King from below
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if 0 <= r < size and 0 <= c < size and grid[r][c] == "P":
            return True

    # Sliding pieces: look for the first piece in each direction
    directions = [
        ((-1, -1), "BQ"), ((-1, 1), "BQ"), ((1, -1), "BQ"), ((1, 1), "BQ"),
        ((-1, 0), "RQ"), ((1, 0), "RQ"), ((0, -1), "RQ"), ((0, 1), "RQ"),
    ]
    for (dr, dc), attackers in directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            ch = grid[r][c]
            if ch in PIECES:
                if ch in attackers:
                    return True
                break
            r += dr
            c += dc
    return False


def checkmate(board):
    try:
        grid = _parse(board)
        if grid is None:
            return
        king = _find_king(grid)
        if king is None:
            return
        if _is_in_check(grid, king[0], king[1]):
            print("Success")
        else:
            print("Fail")
    except Exception:
        return