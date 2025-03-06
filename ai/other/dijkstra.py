class Node:
    def __init__(self,name,conns):
        self.name = name
        self.conns = conns

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"

kvmap = {
    A : [[C,2],[B,4]],
    B : [[C,3],[D,2],[E,3]],
    C : [[B,1],[E,5],[D,4]],
    D : [],
    E : [[D,1]]
}

INIT_NODE = Node(A,kvmap[A])

def main():
    CURRENT_NODE = INIT_NODE
    queue = []
    distances = {
        A: 0
    }
    while True:
        SHORTEST_PATH = 10000
        for conn in CURRENT_NODE.conns:
            if(conn[1]<SHORTEST_PATH):
                SHORTEST_PATH = conn

if __name__ == "__main__":
    main()



