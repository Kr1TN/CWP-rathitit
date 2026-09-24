PIECES = "KQBRP"
NAMES = {"P": "Pawn", "B": "Bishop", "R": "Rook", "Q": "Queen"}

DIAGONALS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
STRAIGHTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def parse_board(board):
    """แปลงกระดานเป็น list ของแถว คืน None ถ้ากระดานไม่ถูกต้อง"""
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
    if sum(line.count("K") for line in lines) != 1:
        return None
    return lines


def find_king(grid):
    for r, row in enumerate(grid):
        c = row.find("K")
        if c != -1:
            return r, c
    return None


def find_attackers(grid, kr, kc):
    """คืน list ของ (ชื่อหมาก, แถว, คอลัมน์, ช่องที่อยู่ระหว่างทาง)"""
    size = len(grid)
    attackers = []

    # Pawn กินเฉียงขึ้น จึงรุก King ได้จากแถวล่างของ King
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if 0 <= r < size and 0 <= c < size and grid[r][c] == "P":
            attackers.append(("P", r, c, []))

    for dirs, valid in ((DIAGONALS, "BQ"), (STRAIGHTS, "RQ")):
        for dr, dc in dirs:
            r, c = kr + dr, kc + dc
            path = []
            while 0 <= r < size and 0 <= c < size:
                ch = grid[r][c]
                if ch in PIECES:
                    if ch in valid:
                        attackers.append((ch, r, c, path))
                    break
                path.append((r, c))
                r += dr
                c += dc
    return attackers


def is_in_check(grid):
    kr, kc = find_king(grid)
    return len(find_attackers(grid, kr, kc)) > 0


def check_board(board):
    """คืน True (โดนรุก), False (ไม่โดนรุก) หรือ None (กระดานไม่ถูกต้อง)"""
    try:
        grid = parse_board(board)
        if grid is None:
            return None
        return is_in_check(grid)
    except Exception:
        return None


def checkmate(board):
    """ฟังก์ชันหลักจาก ex00: พิมพ์ Success / Fail, กระดานผิดไม่พิมพ์อะไร"""
    result = check_board(board)
    if result is True:
        print("Success")
    elif result is False:
        print("Fail")


# ---------------------------------------------------------------------------
# ส่วน creative: อธิบายว่าใครรุก King และ King หนีไปไหนได้บ้าง
# ---------------------------------------------------------------------------

def safe_moves(grid):
    """ช่องที่ King เดินไปได้ (1 ช่องรอบตัว รวมถึงกินหมากศัตรู) โดยไม่โดนรุก"""
    size = len(grid)
    kr, kc = find_king(grid)
    moves = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r, c = kr + dr, kc + dc
            if not (0 <= r < size and 0 <= c < size):
                continue
            rows = [list(row) for row in grid]
            rows[kr][kc] = "."
            rows[r][c] = "K"
            if not is_in_check(["".join(row) for row in rows]):
                captured = grid[r][c] if grid[r][c] in NAMES else None
                moves.append((r, c, captured))
    return moves


def pos(r, c):
    return f"(row {r + 1}, col {c + 1})"


def explain(board):
    """คืนข้อความอธิบายสถานการณ์บนกระดาน หรือ None ถ้ากระดานไม่ถูกต้อง"""
    try:
        grid = parse_board(board)
        if grid is None:
            return None
        kr, kc = find_king(grid)
        attackers = find_attackers(grid, kr, kc)
        moves = safe_moves(grid)

        marks = {}
        for _, r, c, path in attackers:
            for p in path:
                marks[p] = "*"
        view = []
        for r, row in enumerate(grid):
            view.append("  " + " ".join(marks.get((r, c), ch if ch in PIECES else ".")
                                        for c, ch in enumerate(row)))

        out = [f"  King at {pos(kr, kc)}"]
        if attackers:
            for p, r, c, _ in attackers:
                out.append(f"  attacked by {NAMES[p]} at {pos(r, c)}")
        else:
            out.append("  no piece attacks the King")
        out.append("")
        out.extend(view)
        out.append("")
        if moves:
            out.append("  safe moves for King:")
            for r, c, cap in moves:
                extra = f"  (captures {NAMES[cap]})" if cap else ""
                out.append(f"    -> {pos(r, c)}{extra}")
        else:
            out.append("  King has no safe move")
        if attackers and not moves:
            out.append("  >>> CHECKMATE <<<")
        elif not attackers and not moves:
            out.append("  >>> STALEMATE <<<")
        return "\n".join(out)
    except Exception:
        return None
