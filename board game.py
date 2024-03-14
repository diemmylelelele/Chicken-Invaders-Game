def get_winner(game_state):
    rows = len(game_state)
    cols = len(game_state[0])

    # Check rows
    for row in range(rows):
        for col in range(cols - 4):
            if game_state[row][col] != "" and all(game_state[row][col+i] == game_state[row][col] for i in range(1, 5)):
                if (col == 0 or game_state[row][col - 1] != game_state[row][col]) and (col + 4 == cols - 1 or game_state[row][col + 5] != game_state[row][col]):
                    return game_state[row][col]

    # Check columns
    for col in range(cols):
        for row in range(rows - 4):
            if game_state[row][col] != "" and all(game_state[row+i][col] == game_state[row][col] for i in range(1, 5)):
                if (row == 0 or game_state[row - 1][col] != game_state[row][col]) and (row + 4 == rows - 1 or game_state[row + 5][col] != game_state[row][col]):
                    return game_state[row][col]

    # Check diagonals (top-left to bottom-right)
    for row in range(rows - 4):
        for col in range(cols - 4):
            if game_state[row][col] != "" and all(game_state[row+i][col+i] == game_state[row][col] for i in range(1, 5)):
                if ((row == 0 or col == 0) or game_state[row - 1][col - 1] != game_state[row][col]) and ((row + 4 == rows - 1 or col + 4 == cols - 1) or game_state[row + 5][col + 5] != game_state[row][col]):
                    return game_state[row][col]

    # Check diagonals (top-right to bottom-left)
    for row in range(rows - 4):
        for col in range(4, cols):
            if game_state[row][col] != "" and all(game_state[row+i][col-i] == game_state[row][col] for i in range(1, 5)):
                if ((row == 0 or col == cols - 1) or game_state[row - 1][col + 1] != game_state[row][col]) and ((row + 4 == rows - 1 or col - 4 == 0) or game_state[row + 5][col - 5] != game_state[row][col]):
                    return game_state[row][col]

    return "none"

# Example game states 
game_state1 =([["", "", "w", "", "", ""], ["", "b", "w", "", "", ""], ["", "", "w", "b", "", ""], ["", "", "w", "", "", ""], ["", "b", "w", "", "", ""], ["", "", "b", "", "", ""], ["", "", "", "b", "", ""]])
game_state2 =([["", "", "w", "", "", ""], ["", "", "w", "", "", ""], ["w", "b", "b", "b", "b", "b"],["", "", "w", "", "", ""],["", "", "w", "", "", ""],["", "", "", "", "", ""]])
game_state3 =([["", "", "", "", "", ""], ["", "", "", "", "", "w"], ["", "", "b", "", "w", ""], ["", "", "", "w", "", ""], ["", "b", "w", "", "", ""], ["", "w", "b", "", "", ""], ["b", "", "", "b", "", ""]])
game_state4 =([["w", "", "", "", "", ""], ["", "b", "", "", "", ""], ["", "", "b", "", "w", ""], ["", "", "w", "b", "", ""], ["", "", "w", "", "b", ""], ["", "w", "", "", "", "b"], ["", "", "", "", "", ""]])
game_state5 = [["", "", "", "", "", "", ""], ["w", "b", "b", "b", "b", "b", "w"], ["", "w", "", "", "", "", ""], ["", "", "w", "", "", "", ""], ["", "", "", "w", "", "", ""], ["", "", "", "", "w", "", ""], ["", "", "", "", "", "b", ""], ["", "", "", "", "", "", ""]]
game_state6 =([["", "", "", "", "", "", "", "", ""], ["", "b", "w", "w", "w", "w", "w", "", "b"], ["", "", "b", "w", "b", "b", "", "w", ""], ["", "", "", "b", "", "", "b", "", ""], ["", "", "", "", "", "", "", "", ""]])
game_state7 = [["w", "", "", "", "", "", ""], ["", "b", "", "", "", "", ""], ["", "", "b", "", "", "", ""], ["", "", "w", "b", "", "", ""], ["", "", "w", "", "b", "", ""], ["", "w", "", "", "", "b", ""], ["", "", "", "", "", "", "w"], ["", "", "", "", "", "", ""]]
game_state8 =([["w", "", "", "", "", "", ""], ["", "b", "", "", "", "", ""], ["", "", "b", "", "", "", ""], ["", "", "w", "b", "", "", ""], ["", "", "w", "", "b", "", ""], ["", "w", "w", "", "", "b", ""], ["", "", "w", "", "", "", "b"], ["", "", "", "", "", "", ""]])
game_state9 = ([["", "", "", "", "", "", "", "", ""], ["", "b", "", "", "", "w", "", "", ""], ["", "", "b", "w", "b", "", "", "", ""], ["", "", "w", "b", "b", "", "b", "b", ""], ["", "", "w", "", "b", "", "", "", ""], ["", "w", "w", "", "", "w", "", "", ""], ["", "", "w", "", "", "", "", "", ""]])
# Check the results

game_states = [game_state1, game_state2, game_state3, game_state4, game_state5, game_state6, game_state7, game_state8, game_state9 ]
for i, state in enumerate(game_states):
    result = get_winner(state)
    print("Result for game state", i+1, ":", result)