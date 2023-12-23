from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the board, scores, and current player
board = [''] * 9
scores = {'X': 0, 'O': 0}
current_player = 'X'
winner = None


def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != '':
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != '':
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != '':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != '':
        return board[2]

    return None


@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player, winner=winner, scores=scores)


@app.route('/move/<int:position>')
def make_move(position):
    global current_player, winner

    if board[position] == '' and winner is None:
        board[position] = current_player
        winner = check_winner()

        if winner is None:
            # Switch player if the game is still ongoing
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            # Update scores if there's a winner
            scores[winner] += 1

    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    global board, current_player, winner
    board = [''] * 9
    current_player = 'X'
    winner = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
