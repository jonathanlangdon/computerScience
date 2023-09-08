# checks to see if there is a connect-4 winner


def check_horiz(board):
    for row in board:
        middle = row[3]
        if middle == None:
            continue
        continuous = 0
        for spot in row:
            if spot != middle:
                continuous = 0
            else:
                continuous += 1
                if continuous == 4:
                    return middle
    return None


def check_vert(board):
    column_track = [0, 0, 0, 0, 0, 0, 0]
    for row in board:
        for i in range(7):
            if row[i] == board[3][i] and row[i] == board[4][i]:
                column_track[i] += 1
                if column_track[i] == 4:
                    return row[i]
            else:
                column_track[i] = 0
    return None


def check_diagonal(list):
    for line in list:
        if len(line) < 4:
            continue
        count = 0
        for spot in line:
            if line[3] == spot:
                count += 1
                if count == 4:
                    return spot
            else:
                count = 0
    return None


def check_diag_groups_se(board):
    new_groups = [[] for _ in range(12)]
    for i in range(6):
        for j in range(7):
            new_groups[j + 5 - i].append(board[i][j])
    return check_diagonal(new_groups)


def check_diag_groups_ne(board):
    new_groups = [[] for _ in range(12)]
    for i in range(6):
        for j in range(7):
            new_groups[11 - j - i].append(board[i][j])
    return check_diagonal(new_groups)


def check_winner(board):
    result = check_horiz(board)
    if result != None:
        return result
    result = check_vert(board)
    if result != None:
        return result
    result = check_diag_groups_ne(board)
    if result != None:
        return result
    result = check_diag_groups_se(board)
    if result != None:
        return result
    return None


xwins = (
    (None, None, None, None, None, None, None),
    (None, None, None, None, None, None, None),
    (None, None, None, None, "X", None, None),
    (None, None, None, "X", "O", "O", None),
    (None, "O", "X", "X", "O", "X", None),
    ("O", "X", "O", "O", "O", "X", "X"),
)
owins = (
    (None, None, None, None, None, None, None),
    (None, None, None, None, None, None, None),
    ("O", "O", "O", "O", None, None, None),
    ("O", "X", "X", "X", None, None, None),
    ("X", "X", "X", "O", "X", None, None),
    ("X", "O", "O", "X", "O", None, None),
)
nowins = (
    ("X", "X", None, None, None, None, None),
    ("O", "O", None, None, None, None, None),
    ("O", "X", "O", "O", None, "O", "O"),
    ("O", "X", "X", "X", None, "X", "X"),
    ("X", "X", "X", "O", "X", "X", "O"),
    ("X", "O", "O", "X", "O", "X", "O"),
)

print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))
