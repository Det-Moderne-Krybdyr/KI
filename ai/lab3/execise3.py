import heapq

# Define initial environment
LOCATIONS = ['A', 'B', 'C', 'D']

def is_goal(state):
    # Goal is: all rooms clean
    return all(s == 'Clean' for s in state[1:])

def heuristic(state):
    # Heuristic = number of dirty rooms left
    return sum(1 for s in state[1:] if s == 'Dirty')

def vacuum_successors(state):
    loc, a, b, c, d = state
    successors = []

    # Suck action
    if loc == 'A' and a == 'Dirty':
        successors.append((('A', 'Clean', b, c, d), 'Suck', 1))
    elif loc == 'B' and b == 'Dirty':
        successors.append((('B', a, 'Clean', c, d), 'Suck', 1))
    elif loc == 'C' and c == 'Dirty':
        successors.append((('C', a, b, 'Clean', d), 'Suck', 1))
    elif loc == 'D' and d == 'Dirty':
        successors.append((('D', a, b, c, 'Clean'), 'Suck', 1))

    # Movement (from original model)
    moves = {
        'A': [('B', 'Right'), ('C', 'Down')],
        'B': [('A', 'Left'), ('D', 'Down')],
        'C': [('A', 'Up'), ('D', 'Right')],
        'D': [('B', 'Up'), ('C', 'Left')]
    }

    for dest, action in moves[loc]:
        successors.append(((dest, a, b, c, d), action, 1))

    return successors

def a_star_vacuum(initial_state):
    frontier = []
    heapq.heappush(frontier, (heuristic(initial_state), 0, initial_state, [], 0))  # (f, g, state, path, cost)
    explored = set()
    explored_nodes = 0

    while frontier:
        f, g, state, path, cost = heapq.heappop(frontier)

        if is_goal(state):
            return path + [state], cost, explored_nodes

        if state in explored:
            continue
        explored.add(state)
        explored_nodes += 1

        for next_state, action, step_cost in vacuum_successors(state):
            if next_state not in explored:
                new_cost = cost + step_cost
                new_path = path + [state]
                priority = new_cost + heuristic(next_state)
                heapq.heappush(frontier, (priority, new_cost, next_state, new_path, new_cost))

    return None, None, None

def run():
    initial_state = ('A', 'Dirty', 'Dirty', 'Dirty', 'Dirty')
    path, cost, explored = a_star_vacuum(initial_state)

    print("\n✅ A* Vacuum Cleaner – Solution")
    print("Path to goal:")
    for step in path:
        print(step)
    print(f"\nTotal cost (number of moves): {cost}")
    print(f"Number of explored nodes: {explored}")

if __name__ == "__main__":
    run()
