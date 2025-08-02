import streamlit as st

# Title of the game
st.title("Tic-Tac-Toe Game")

# Initialize the game state in session
if "board" not in st.session_state:
    # 3x3 grid with empty spaces
    st.session_state.board = [[" "]*3 for _ in range(3)]
    st.session_state.turn = "X"  # Player X starts
    st.session_state.game_over = False  # Game state tracker

# Function to check if the current player has won
def check_winner(board, player):
    # Check rows for win
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[r][col] == player for r in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Draw the 3x3 board using columns
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        # Display buttons for each cell
        if cols[j].button(st.session_state.board[i][j] or " ", key=f"{i}{j}"):
            # If game is not over and cell is empty
            if not st.session_state.game_over and st.session_state.board[i][j] == " ":
                # Make the move
                st.session_state.board[i][j] = st.session_state.turn

                # Check if this move wins the game
                if check_winner(st.session_state.board, st.session_state.turn):
                    st.success(f"🎉 Player {st.session_state.turn} wins!")
                    st.session_state.game_over = True
                else:
                    # Check if the board is full (draw)
                    all_filled = all(cell != " " for row in st.session_state.board for cell in row)
                    if all_filled:
                        st.warning("It's a draw!")
                        st.session_state.game_over = True
                    else:
                        # Switch turns
                        st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

# Button to restart the game
if st.button("Restart Game"):
    st.session_state.board = [[" "]*3 for _ in range(3)]
    st.session_state.turn = "X"
    st.session_state.game_over = False
