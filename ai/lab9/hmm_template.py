import numpy as np

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a describtion of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 3, 3, 1, 2],
    ]

    # Markov transition matrix
    # transitions[start, end] I   H   C   F
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q)
    # emission[state, observation]
    #                       0   1   2   3   ice creams 
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(str(path))))

        print('')


def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 has mea1ning in the matrix
    forward = np.ones((big_n + 2, big_t + 1)) * 5
    
    
    # init step
    for j in range(1,big_n+1):
        forward[j,1]=transitions[0,j]*emissions[j,observations[1]]

    #recursion 
    for t in range (2,big_t+1):
        for j in range(1,big_n+1):
            sum = 0
            for i in range(1,big_n+1):
                sum += forward[i,t-1] * transitions[i,j]
            forward[j,t] = sum*emissions[j,observations[t]]
    #termination
    sum=0
    for i in range(1,big_n+1):
        sum+=forward[i,big_t]*transitions[i,f]
    
    print(forward)
    print("sum: " + str(sum))
    '''
    FINISH FUNCITON
    '''
    
    return sum

def compute_viterbi(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 is valid value in matrix
    viterbi = np.ones((big_n + 2, big_t + 1)) * 5

    # Must be of type int, otherwise it is tricky to use its elements to index
    # the states
    # all values initialized to 5, as 0 is valid value in matrix
    backpointers = np.ones((big_n + 2, big_t + 1), dtype=int) * 5

    #init
    for j in range(1,big_n+1):
        viterbi[j,1] = transitions[0,j]*emissions[j,observations[1]]
        backpointers[j,1] = 0

    #recursion
    for t in range(2,big_t+1):
        for j in range(1,big_n+1):
            max = 0
            bp = 5
            for i in range(1,big_n+1):
                val = viterbi[i,t-1]*transitions[i,j]*emissions[j,observations[t]]
                if(val>=max):
                    max = val
                    bp = i
            backpointers[j,t] = bp
            viterbi[j,t] = max
 
    #termination
    li = []
    bigger = 0
    last_state = 0
    for i in range(1,big_n+1):
        state = viterbi[i,big_t]
        if state > bigger:
            last_state = i
            bigger = state


    li.append(last_state)
    #backtrace
    bigger = 0
    for t in range(big_t,1,-1):
        last_state = backpointers[last_state,t]
        li.append(int(last_state))
    li.reverse()
    print(viterbi)
    print(backpointers)
    return li
    '''
    FINISH FUNCTION
    '''

    


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))

    # Since we loop from 1 to big_n, the result of argmax is between
    # 0 and big_n - 1. However, 0 is the initial state, the actual
    # states start from 1, so we add 1.
    return 1 + max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
