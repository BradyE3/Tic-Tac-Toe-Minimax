# Import necessary functions from the board module
from board import create_board, track_turn, win_conditions, ai_bot_minimax

# Dictionary to store the game board positions (numbers 1 to 9 represent spots on the board)
spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

# Variable to control the game loop
game = True

# Variable to track the number of turns taken in the game
turn_count = 0

# List to store the player inputs (to check if a spot is already chosen)
inputs = []

# Game loop, continues until the game is over
while game:
    # print(turn_count)  # Uncomment this line if you need to debug turn_count

    # Display the current game board
    create_board(spots)

    # Ask the current player for their choice
    player_choice = input("What's your play: ")

    # Check if this is the first move (no inputs yet)
    if len(inputs) == 0:
        # Update the spot on the board with the player's symbol (X or O)
        spots[int(player_choice)] = "X"

        # Add the current choice to the list of inputs
        inputs.append(player_choice)

    # If it's not the first move and the spot is not already chosen
    elif player_choice not in inputs:
        # Update the spot on the board with the player's symbol (X or O)
        spots[int(player_choice)] = "X"

        # Add the current choice to the list of inputs
        inputs.append(player_choice)

    else:
        # The chosen spot is already taken, prompt the player to pick another spot
        print("Pick another space")

    # Check for a win condition after each player's move
    if win_conditions(spots, "X"):
        create_board(spots)
        print("Player X wins!")
        game = False

    # Use the ai_bot function to make the AI's move
    elif ai_bot_minimax(spots, inputs):
        print("Computer Wins")
        game = False

    # If no win condition is met and the board is full, it's a draw
    elif turn_count == 9:
        create_board(spots)
        print("It's a draw!")
        game = False
