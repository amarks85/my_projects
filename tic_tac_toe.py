import random as rd

row_list = [2, 6, 10]  # row number to access values in board
col_list = [4, 12, 20]  # column number to access values in board

board: list = []
marked_box_list = [5]
match_result = "Draw"

# Initialize the board list
for a in range(13):
    new = []
    for b in range(25):
        new.append(b)
    board.append(new)


# Initialize display board
def init_display_board():
    for i in range(13):
        for j in range(25):
            if i == 0 or i == 4 or i == 8 or i == 12:
                if j % 8 == 0:
                    board[i][j] = "+"
                else:
                    board[i][j] = "-"
            else:
                if j % 8 == 0:
                    board[i][j] = "|"
                else:
                    board[i][j] = " "
    q = 1
    for x in [2, 6, 10]:
        for y in [4, 12, 20]:
            if q != 5:
                board[x][y] = q
            else:
                board[x][y] = "X"
            q += 1
    for k in range(13):
        for m in range(25):
            print(board[k][m], end="")
        print("\n", end="")


def update_board(num, ip_info):
    found_num = False
    for x in row_list:
        for y in col_list:
            if board[x][y] == num:
                if ip_info == "usr":
                    board[x][y] = "O"
                elif ip_info == "comp":
                    board[x][y] = "X"
                found_num = True
                break
        if found_num:
            break
    for k in range(13):
        for m in range(25):
            print(board[k][m], end="")
        print("\n", end="")


def calc_comp_move():
    while True:
        val = rd.randrange(1, 10)
        if val in marked_box_list:
            continue
        else:
            return val


def check_game_status(ip):
    if ip == "usr":
        for i in row_list:
            if board[i][col_list[0]] == board[i][col_list[1]] == board[i][col_list[2]] == "O":
                return True

        for j in col_list:
            if board[row_list[0]][j] == board[row_list[1]][j] == board[row_list[2]][j] == "O":
                return True

    if ip == "comp":
        for i in row_list:
            if board[i][col_list[0]] == board[i][col_list[1]] == board[i][col_list[2]] == "X":
                return True

        for j in col_list:
            if board[row_list[0]][j] == board[row_list[1]][j] == board[row_list[2]][j] == "X":
                return True

        if board[2][4] == board[10][20] == "X" or board[2][20] == board[10][4] == "X":
            return True


def main():
    global match_result
    init_display_board()
    for i in range(4):
        n = int(input("Enter your move: "))
        if n not in marked_box_list:
            marked_box_list.append(n)
            update_board(n, "usr")
            status = check_game_status("usr")
            if status:
                match_result = "User Won"
                break
            m = calc_comp_move()
            update_board(m, "comp")
            marked_box_list.append(m)
            status = check_game_status("comp")
            if status:
                match_result = "Computer Won"
                break
    print(match_result)


if __name__ == "__main__":
    main()
