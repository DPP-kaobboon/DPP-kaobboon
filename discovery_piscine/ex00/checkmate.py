def checkmate(board):

    if isinstance(board, str):
        board = [line.strip() for line in board.strip().split('\n') if line.strip()]

    rows = len(board)
    if rows == 0:
        print("Fail")
        return

    if any(len(row) != rows for row in board):
        print("Fail")
        return

    cols = len(board[0])

    king_r, king_c = -1, -1
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'K':
                king_r, king_c = r, c
                break
        if king_r != -1:
            break
    if king_r == -1:
        print("Fail")
        return

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def is_empty(cell):
        return (
            cell == '.'
            or isinstance(cell, (int, float))
            or (
                isinstance(cell, str)
                and (
                    cell.isdigit()
                    or (cell.isalpha() and cell not in 'PBRQK')
                )
            )
        )

    pawn_attack_offsets = [(1, -1), (1, 1)]
    for dr, dc in pawn_attack_offsets:
        r, c = king_r + dr, king_c + dc
        if is_valid(r, c) and board[r][c] == 'P':
            print("Success")
            return

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        r, c = king_r + dr, king_c + dc
        while is_valid(r, c):
            piece = board[r][c]
            if not is_empty(piece):
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break 
            r += dr
            c += dc

    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        r, c = king_r + dr, king_c + dc
        while is_valid(r, c):
            piece = board[r][c]
            if not is_empty(piece):
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break 
            r += dr
            c += dc

    print("Fail")