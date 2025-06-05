import functools
from itertools import product


# Core utility
def multiply_vector_elements(vector):
    return functools.reduce(lambda x, y: x * y, vector, 1)


# Variable class
class Variable:
    def __init__(self, name, assignments, probability_table, parents=None):
        self.name = name
        self.assignments = {k: i for i, k in enumerate(assignments)}
        self.reverse_assignments = {i: k for k, i in self.assignments.items()}
        self.probability_table = probability_table
        self.parents = parents or []
        self.marginal_probabilities = [0] * len(assignments)
        self.ready = False

    def get_probability(self, value, parents_values):
        return self.probability_table[parents_values][self.assignments[value]]

    def calculate_marginal_probability(self):
        if self.ready:
            return
        if not self.parents:
            self.marginal_probabilities = list(self.probability_table[()])
        else:
            total = [0] * len(self.assignments)
            parent_domains = [p.assignments.keys() for p in self.parents]
            for combo in product(*parent_domains):
                parent_vals = dict(zip([p.name for p in self.parents], combo))
                p_joint = 1
                for p in self.parents:
                    p.calculate_marginal_probability()
                    p_joint *= p.get_marginal_probability(parent_vals[p.name])
                probs = self.probability_table[
                    tuple(parent_vals[p.name] for p in self.parents)
                ]
                for i in range(len(probs)):
                    total[i] += probs[i] * p_joint
            self.marginal_probabilities = total
        self.ready = True

    def get_marginal_probability(self, val):
        return self.marginal_probabilities[self.assignments[val]]


class BayesianNetwork:
    def __init__(self):
        self.variables = []
        self.varsMap = {}

    def set_variables(self, var_list):
        self.variables = var_list
        self.varsMap = {v.name: v for v in var_list}

    def calculate_marginal_probabilities(self):
        for var in self.variables:
            var.calculate_marginal_probability()

    def get_joint_probability(self, values):
        missing = [v.name for v in self.variables if v.name not in values]
        if not missing:
            prob = 1
            for var in self.variables:
                val = values[var.name]
                parent_vals = tuple(values[p.name] for p in var.parents)
                prob *= var.get_probability(val, parent_vals)
            return prob
        # Marginalize missing
        domains = {v.name: list(v.assignments.keys()) for v in self.variables}
        total = 0
        for assignment in product(*[domains[v] for v in missing]):
            full_values = {**values, **dict(zip(missing, assignment))}
            total += self.get_joint_probability(full_values)
        return total

    def get_conditional_probability(self, values, evidents):
        joint = self.get_joint_probability({**values, **evidents})
        var_name = list(values.keys())[0]
        denom = 0
        for alt_val in self.varsMap[var_name].assignments:
            new_values = values.copy()
            new_values[var_name] = alt_val
            denom += self.get_joint_probability({**new_values, **evidents})
        return joint / denom if denom > 0 else 0


# Display helpers
def print_marginals(network):
    print("Marginal probabilities:")
    for var in network.variables:
        for val in var.assignments:
            prob = var.get_marginal_probability(val)
            print(f"P({var.name}={val}) = {prob:.6f}")


def print_conditional(network, values, evidents):
    prob = network.get_conditional_probability(values, evidents)
    print(f"P({list(values.items())[0]} | {evidents}) = {prob:.6f}")


# === TEMPLATE FILL-IN SECTION ===
def exam_setup():
    # CPTs
    t1 = {(): (0.3, 0.7)}  # Example P(DT)
    t2 = {(): (0.2, 0.8)}  # P(FTL)
    t3 = {(): (0.3, 0.7)}  # P(EM)

    t4 = {
        ("true",): (0.7, 0.3),  # P(V | DT)
        ("false",): (0.1, 0.9),
    }

    t5 = {
        ("true", "true"): (0.05, 0.95),  # P(SMS | DT, EM)
        ("true", "false"): (0.6, 0.4),
        ("false", "true"): (0.3, 0.7),
        ("false", "false"): (0.7, 0.3),
    }

    t6 = {
        ("true", "true", "true"): (0.9, 0.1),  # P(HC | DT, FTL, EM)
        ("true", "true", "false"): (0.8, 0.2),
        ("true", "false", "true"): (0.3, 0.7),
        ("true", "false", "false"): (0.2, 0.8),
        ("false", "true", "true"): (0.6, 0.4),
        ("false", "true", "false"): (0.5, 0.5),
        ("false", "false", "true"): (0.1, 0.9),
        ("false", "false", "false"): (0.01, 0.99),
    }

    # Define Variables
    DT = Variable("DT", ("true", "false"), t1)
    FTL = Variable("FTL", ("true", "false"), t2)
    EM = Variable("EM", ("true", "false"), t3)
    V = Variable("V", ("true", "false"), t4, [DT])
    SMS = Variable("SMS", ("true", "false"), t5, [DT, EM])
    HC = Variable("HC", ("true", "false"), t6, [DT, FTL, EM])

    # Build network
    net = BayesianNetwork()
    net.set_variables([DT, FTL, EM, V, SMS, HC])
    net.calculate_marginal_probabilities()

    # Homework evidence (just plug in your own!)
    evidence = {"V": "true", "SMS": "true", "HC": "false"}

    # Print what’s relevant
    print_marginals(net)
    print()
    print_conditional(net, {"DT": "true"}, evidence)
    print_conditional(net, {"EM": "true"}, evidence)
    print_conditional(net, {"FTL": "true"}, evidence)


# Run it
exam_setup()
