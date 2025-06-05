def fitness_fn_positive(state):
    """
    Compute the number of non-conflicting pairs among queens.
    Higher is better. Max = 28 for 8-queens.
    """
    n = len(state)
    max_pairs = n * (n - 1) // 2
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            same_row = state[i] == state[j]
            same_diag = abs(state[i] - state[j]) == abs(i - j)
            if same_row or same_diag:
                conflicts += 1

    return max_pairs - conflicts
