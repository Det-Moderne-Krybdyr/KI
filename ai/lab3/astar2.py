class Node:
    def __init__(self,state):
        self.STATE = state
        self.OPTIMAL_PARENT = None
        self.COST = 0
    def __repr__(self):
        return self.STATE.NAME
    def display(self):
        print(self)
    def path(self):
        current_node = self
        path = [self]
        while current_node.OPTIMAL_PARENT:
            current_node = current_node.OPTIMAL_PARENT 
            path.append(current_node)
        return path
class UNode:
    def __init__(self,name,heuristic):
        self.NAME = name
        self.HEURISTIC = heuristic

def main():
    queue = []
    init_node = Node(INITIAL_STATE)
    INSERT_QUEUE(init_node,queue)
    while len(queue) != 0:
        node = REMOVE_QUEUE(queue)
        if node.STATE == GOAL_STATE:
            print("path is" + str(node.path()))
            return
        children = EXPAND(node,queue)
        queue = INSERT_ALL(children,queue)
        print("Current queue: {}\n\n".format(queue))

def EXPAND(node,queue):
    print("Expanding: " + str(node.STATE.NAME))
    successors = []
    children = STATE_SPACE[node.STATE]
    for child in children:
        f = IS_DISCOVERED(child[0],queue)
        if(f):
            if(f>child[1]+node.COST+child[0].HEURISTIC):
                s = Node(node)
                s.STATE = child[0]
                s.COST = child[1]+node.COST
                s.OPTIMAL_PARENT = node
                REPLACE_IN_QUEUE(s,queue)
        else:
            s = Node(node)
            s.STATE = child[0]
            s.COST = child[1]+node.COST
            s.OPTIMAL_PARENT = node
            successors.append(s)
    return successors



def INSERT_QUEUE(node,queue):
    queue.append([node,node.COST+node.STATE.HEURISTIC])
    queue.sort(key=lambda x: x[1])

def INSERT_ALL(list,queue):
    for e in list:
        INSERT_QUEUE(e,queue)
    queue.sort(key=lambda x:x[1])
    return queue

def REPLACE_IN_QUEUE(node,queue):
    for i in range(0,len(queue)):
        if(queue[i][0].STATE == node.STATE):
            queue[i][0] = node
            queue[i][1] = node.COST + node.STATE.HEURISTIC
    queue.sort(key=lambda x: x[1])

def IS_DISCOVERED(state,queue):
    for i in range(0,len(queue)):
        if (queue[i][0].STATE == state):
            return queue[i][1]
    return False

def REMOVE_QUEUE(queue):
    element = queue.pop(0)
    return element[0]



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
GOAL_STATE = K
STATE_SPACE = {
                A:[[B,1],[C,2],[D,4]],
                B:[[F,5],[E,4]],
                C:[[E,1]],
                D:[[H,1],[I,4],[J,2]],
                E:[[G,2],[H,3]],
                F:[[G,1]],
                G:[[K,6]],
                H:[[K,6],[L,5]],
                I:[[L,3]],
                J:[],
                K:[],
                L:[]
               }

if __name__ == "__main__":
    main()