import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---|---|---")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

def check_winner(brd, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for cond in win_conditions:
        if all(brd[i] == player for i in cond):
            return True
    return False

def is_board_full():
    return ' ' not in board

def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    if check_winner(brd, 'X'):
        return -1
    if ' ' not in brd:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe")
    print("You are 'X', AI is 'O'")
    print_board()

    while True:
        # Human move
        try:
            human_move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input Enter a number between 1-9.")
            continue

        if human_move not in available_moves():
            print("Invalid move Try again.")
            continue

        board[human_move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("Congratulations You win")
            break
        if is_board_full():
            print("It's a draw")
            break

        # AI move
        print("AI is making a move...")
        ai_move = best_move()
        board[ai_move] = 'O'
        print_board()

        if check_winner(board, 'O'):
            print("AI wins Better luck next time.")
            break
        if is_board_full():
            print("It's a draw")
            break

if __name__ == "__main__":
    play_game()
