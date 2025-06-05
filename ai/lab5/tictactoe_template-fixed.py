def minmax_decision(state):
    infinity = float("inf")

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for a, s in successors_of(state, "X"):
            v = max(v, min_value(s))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for a, s in successors_of(state, "O"):
            v = min(v, max_value(s))
        return v

    action, _ = argmax(successors_of(state, "X"), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    return (
        is_winner(state, "X")
        or is_winner(state, "O")
        or all(s in ["X", "O"] for s in state)
    )


def is_winner(state, s):
    return any(
        [
            state[0] == state[1] == state[2] == s,
            state[3] == state[4] == state[5] == s,
            state[6] == state[7] == state[8] == s,
            state[0] == state[3] == state[6] == s,
            state[1] == state[4] == state[7] == s,
            state[2] == state[5] == state[8] == s,
            state[0] == state[4] == state[8] == s,
            state[2] == state[4] == state[6] == s,
        ]
    )


def utility_of(state):
    if is_winner(state, "O"):
        return -1
    if is_winner(state, "X"):
        return 1
    return 0


def successors_of(state, player):
    return [
        (i, state[:i] + [player] + state[i + 1 :])
        for i in range(9)
        if state[i] not in ["X", "O"]
    ]


def display(state):
    print("-----")
    for i in range(0, 9, 3):
        print(
            " ".join(
                str(state[j]) if isinstance(state[j], str) else "."
                for j in range(i, i + 3)
            )
        )


def argmax(iterable, func):
    return max(iterable, key=func)


def main():
    board = [i for i in range(9)]
    while not is_terminal(board):
        ai_move = minmax_decision(board)
        board[ai_move] = "X"
        display(board)
        if is_terminal(board):
            break

        move = -1
        while move not in range(9) or board[move] in ["X", "O"]:
            try:
                move = int(input("Your move (0-8)? "))
            except ValueError:
                continue
        board[move] = "O"

    display(board)
    if is_winner(board, "X"):
        print("Computer (X) wins!")
    elif is_winner(board, "O"):
        print("You (O) win!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
