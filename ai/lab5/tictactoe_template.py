def minmax_decision(state):
    infinity = float('inf')

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state,'X'):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state,'O'):
            v = min(v, max_value(s))
        return v

    action, state = argmax(successors_of(state,'X'), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    if is_winner(state,'X') or is_winner(state,'O'):
        return True
    
    for e in state:
        if e != 'X' and e != 'O':
            return False
    
    return True

def is_winner(state,s):
    if state[0] == s and state[1] == s and state[2] == s:
        return True
    if state[3] == s and state[4] == s and state[5] == s:
        return True
    if state[6] == s and state[7] == s and state[8] == s:
        return True
    if state[0] == s and state[3] == s and state[6] == s:
        return True
    if state[1] == s and state[4] == s and state[7] == s:
        return True
    if state[2] == s and state[5] == s and state[8] == s:
        return True
    if state[0] == s and state[4] == s and state[8] == s:
        return True
    if state[2] == s and state[4] == s and state[6] == s:
        return True
    return False

def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    if is_winner(state,'O'):
        return -1
    if is_winner(state,'X'):
        return 1
    return 0


def successors_of(state,player):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    returnList = list()

    for i in range(0,9):
        if state[i] not in ['X','O']:
            newState = state.copy()
            newState[i] = player
            returnList.append((i,newState))
    return returnList


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
