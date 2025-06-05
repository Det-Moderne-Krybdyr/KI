def alpha_beta_decision(state):
    infinity = float("inf")

    def max_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for successor in successors_of(state):
            v = max(v, min_value(successor, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)  # FIXED
        return v

    def min_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for successor in successors_of(state):
            v = min(v, max_value(successor, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)  # FIXED
        return v

    return argmax(successors_of(state), lambda a: min_value(a, -infinity, infinity))


def is_terminal(state):
    # Game is over when no pile is splittable (i.e., all are <= 2)
    return all(pile < 3 for pile in state)


def utility_of(state):
    # MAX wins if MIN cannot move
    return 1 if is_terminal(state) else 0


def successors_of(state):
    """
    Returns a list of valid states from the current state by splitting any pile > 2
    into two unequal, positive parts.
    """
    result = []
    for i, pile in enumerate(state):
        if pile >= 3:
            for j in range(1, pile):
                k = pile - j
                if j != k:
                    new_state = state[:i] + [j, k] + state[i + 1 :]
                    result.append(new_state)
    return result


def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = alpha_beta_decision(state)
    print("Computer splits to: {}".format(new_state))
    return new_state


def user_select_pile(list_of_piles):
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                "How much is the first split (from 1 to {}, but not {})?".format(
                    max_split, list_of_piles[i] // 2
                )
            )
        else:
            print("How much is the first split (from 1 to {})?".format(max_split))
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1 :]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [7]  # or use [15] or [20] for a more challenging test

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))
    print("    No more moves. You lose!")


if __name__ == "__main__":
    main()
