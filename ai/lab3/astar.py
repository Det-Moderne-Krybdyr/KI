class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.COST = 0

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE.NAME) + ' - Depth: ' + str(self.DEPTH) + ' - Cost: ' + str(self.COST)

class UNode:
    def __init__(self,name,heuristic):
        self.NAME = name
        self.HEURISTIC = heuristic
'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while len(fringe) != 0:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child[0]  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.COST += child[1]
        successors = INSERT_SUCCESSORS(s, successors)
    return successors

def INSERT_SUCCESSORS(node,list):
    list.append(node)
    return list

def INSERT(node, queue):
    nodeState = node.STATE
    priority = nodeState.HEURISTIC + node.COST
    queue.append([node,priority])
    queue.sort(key=lambda x: x[1])
    return queue


def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node,queue)
    return queue


def REMOVE_FIRST(queue):
    element = queue.pop(0)
    return element[0]


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]

#order: FARMER,WOLF,GOAT,CABBAGE
#E: east of river W: west of river -> travelling east
A = UNode("A",6)
B = UNode("B",5)
C = UNode("C",5)
D = UNode("D",2)
E = UNode("E",4)
F = UNode("F",5)
G = UNode("G",4)
H = UNode("H",1)
I = UNode("I",2)
J = UNode("J",1)
K = UNode("K",0)
L = UNode("L",0)
INITIAL_STATE = A
GOAL_STATE = L
STATE_SPACE = {
                A:[[B,1],[C,2],[D,4]],
                B:[[F,5],[E,4]],
                C:[[E,1]],
                D:[[H,1],[I,4],[J,2]],
                E:[[G,2],[H,3]],
                G:[[K,6]],
                H:[[K,6],[L,5]],
                I:[[J,2]],
                J:[],
                K:[]
               }


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    print(path)
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
