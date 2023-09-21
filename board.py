import math


def create_board(spots):
    """
    Creates and displays the game board based on the current spots dictionary.
    :param spots: Dictionary containing the current state of the game board.
    """
    board = (
        f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
        f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
        f"|{spots[7]}|{spots[8]}|{spots[9]}|"
    )

    print(board)


def track_turn(turn):
    """
    Tracks the current turn and determines whose turn it is (Player X or Player O).
    :param turn: Integer representing the current turn number.
    :return: 'X' if it's an odd turn, 'O' if it's an even turn.
    """
    if turn % 2 == 0:
        return "O"  # Player O's turn for even turns
    else:
        return "X"  # Player X's turn for odd turns


def win_conditions(spots, player):
    """
    Check if the specified player has won the game.
    :param spots: Dictionary containing the current state of the game board.
    :param player: The symbol of the player to check ('X' or 'O').
    :return: True if the player has won, False otherwise.
    """
    win_combinations = [
        # Rows
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        # Columns
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        # Diagonals
        [1, 5, 9],
        [3, 5, 7],
    ]

    for combination in win_combinations:
        if all(spots[spot] == player for spot in combination):
            return True

    return False


win_combinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],  # Rows
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],  # Columns
    [1, 5, 9],
    [3, 5, 7],  # Diagonals
]


def evaluate_board(spots):
    ai_score = 0
    human_score = 0

    for combination in win_combinations:
        count_ai = sum(1 for spot in combination if spots[spot] == 'O')
        count_human = sum(1 for spot in combination if spots[spot] == 'X')

        if count_ai == 2 and count_human == 0:
            ai_score += 1
        elif count_human == 2 and count_ai == 0:
            human_score += 1

    return ai_score - human_score


def minimax(spots, depth, is_maximizing):
    open_spots = [spot for spot in spots if spots[spot] != "X" and spots[spot] != "O"]

    if win_conditions(spots, 'O'):
        return 1
    if win_conditions(spots, 'X'):
        return -1
    if depth == 0:
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for spot in open_spots:
            if spots[spot] != 'X' and spots[spot] != 'O':
                spots[spot] = 'O'
                eval = minimax(spots, depth - 1, False)
                spots[spot] = str(spot)  # Reset the spot
                max_eval = max(max_eval, eval)
                if eval == 1:
                    break  # Stop checking if the AI can win
        return max_eval
    else:
        min_eval = math.inf
        for spot in open_spots:
            if spots[spot] != 'X' and spots[spot] != 'O':
                spots[spot] = 'X'
                eval = minimax(spots, depth - 1, True)
                spots[spot] = str(spot)  # Reset the spot
                min_eval = min(min_eval, eval)
                if eval == -1:
                    break  # Stop checking if the player can win
        return min_eval



def ai_bot_minimax(spots, inputs):
    open_spots = [spot for spot in spots if spots[spot] != "X" and spots[spot] != "O"]

    best_move = -1
    best_eval = -math.inf

    for spot in open_spots:
        spots[spot] = "O"
        if win_conditions(spots, "O"):
            best_move = spot
            break
        spots[spot] = str(spot)  # Reset the spot

        spots[spot] = "X"
        if win_conditions(spots, "X"):
            best_move = spot
            break
        spots[spot] = str(spot)  # Reset the spot

    if best_move == -1:
        for spot in open_spots:
            spots[spot] = "O"
            move_eval = minimax(spots, 9, False)
            spots[spot] = str(spot)

            if move_eval > best_eval:
                best_eval = move_eval
                best_move = spot

    spots[best_move] = "O"
    inputs.append(best_move)

    print(f"Computer chose spot {best_move}")

    if win_conditions(spots, "O"):
        create_board(spots)
        print("Computer Wins")
        return True

    return False

